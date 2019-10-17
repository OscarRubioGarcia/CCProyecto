package com.example;

import java.util.stream.Stream;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.stereotype.Component;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@EnableDiscoveryClient
@SpringBootApplication
public class StoryServiceApplication 
{

	public static void main(String[] args) 
	{
		SpringApplication.run(StoryServiceApplication.class, args);
	}

}

@Data
@AllArgsConstructor
@NoArgsConstructor
@ToString
@Entity
class Story {

    @Id
    @GeneratedValue
    private Long id;

    private String name;
    private String description;
    
    public Story(String name) 
    {
        this.name = name;
    }
    
    public Story(String name, String description) 
    {
        this.name = name;
        this.description = description;
    }

}

@RepositoryRestResource
interface StoryRepository extends JpaRepository<Story, Long> {}

@Component
class StoryInitializer implements CommandLineRunner 
{

    private final StoryRepository storyRepository;

    StoryInitializer(StoryRepository storyRepository) 
    {
        this.storyRepository = storyRepository;
    }

    @Override
    public void run(String... args) throws Exception 
    {
        Stream.of("Guines", "Don Quijote 2", "Bad Boys", "Powerrangers", "El libro de Petete", "Como conducir vol.2", "Recetas de Cocina")
                .forEach(storyName -> {
                    Story i = new Story(storyName);
                    storyRepository.save(i);
                });
        storyRepository.findAll().forEach(System.out::println);
    }
}