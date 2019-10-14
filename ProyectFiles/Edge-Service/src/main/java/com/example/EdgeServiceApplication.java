package com.example;

import java.util.ArrayList;
import java.util.Collection;
import java.util.stream.Collectors;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.hateoas.Resources;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;

import lombok.Data;

@EnableFeignClients
@EnableCircuitBreaker
@EnableDiscoveryClient
@EnableZuulProxy
@SpringBootApplication
public class EdgeServiceApplication 
{

	public static void main(String[] args) 
	{
		SpringApplication.run(EdgeServiceApplication.class, args);
	}

}

@Data
class Story 
{
    private String name;
    private String description;
    
    public String getName() 
    {
        return name; 
    }

    public void setName(String name) 
    { 
    	this.name = name;
    }
    
    public String getDescription() 
    {
    	return description;
    }
    
    public void setDescription(String description) 
    {
    	this.description = description;
    }
}

@FeignClient("story-service")
interface StoryClient {

    @GetMapping("/stories")
    Resources<Story> readStories();
}

@RestController
class TopStoriesApiAdapterRestController {

    private final StoryClient storyClient;

    public TopStoriesApiAdapterRestController(StoryClient storyClient) 
    {
        this.storyClient = storyClient;
    }

    @HystrixCommand(fallbackMethod = "fallback")
    @GetMapping("/top-stories")
    public Collection<Story> topStories() {
        return storyClient.readStories()
                .getContent()
                .stream()
                .filter(this::isTop)
                .collect(Collectors.toList());
    }

    private boolean isTop(Story story) {
        return !story.getName().equals("Don Quijote 2") &&
                !story.getName().equals("Powerrangers") &&
                !story.getName().equals("El libro de Petete");
    }
    
    public Collection<Story> fallback() {
        Collection<Story> coll = new ArrayList<>();
        Story i = new Story();
        i.setName("Error Book");
        i.setDescription("Error description.");
        coll.add(i);
        return coll;
    }
}
