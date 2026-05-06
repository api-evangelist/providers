---
aid: spring-data
name: Spring Data
description: Spring Data's mission is to provide a familiar and consistent, Spring-based programming model for data access while still retaining the special traits of the underlying data store. It makes it easy to use data access technologies, relational and non-relational databases, map-reduce frameworks, and cloud-based data services. This is an umbrella project which contains many subprojects that are specific to a given database.
type: Index
image: https://spring.io/img/projects/spring-data.svg
url: https://spring.io/projects/spring-data
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Data Access
  - Database
  - Framework
  - Java
  - JPA
  - MongoDB
  - ORM
  - Redis
  - REST
  - Spring
apis:
  - aid: spring-data:spring-data-rest
    name: Spring Data REST
    description: Exports Spring Data repositories as hypermedia-driven RESTful resources automatically. Provides HATEOAS-compliant endpoints with HAL browser, pagination, sorting, projections, and custom event hooks.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-rest
    baseURL: http://localhost:8080
    tags:
      - HATEOAS
      - HAL
      - Hypermedia
      - Repository
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-rest
      - type: API Reference
        url: https://docs.spring.io/spring-data/rest/docs/current/api/
      - type: Getting Started
        url: https://spring.io/guides/gs/accessing-data-rest/
      - type: OpenAPI
        url: openapi/spring-data-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/spring-data-paged-resource-schema.json
      - type: JSONStructure
        url: json-structure/spring-data-hal-resource-structure.json
  - aid: spring-data:spring-data-jpa
    name: Spring Data JPA
    description: Simplifies the development of creating a JPA-based data access layer. Reduces boilerplate code and provides powerful query derivation, named queries, and specification-based querying on top of JPA/Hibernate.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-jpa
    baseURL: http://localhost:8080
    tags:
      - Database
      - Hibernate
      - JPA
      - Persistence
      - Repository
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/jpa/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-jpa
      - type: API Reference
        url: https://docs.spring.io/spring-data/jpa/docs/current/api/
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-jpa
  - aid: spring-data:spring-data-mongodb
    name: Spring Data MongoDB
    description: Provides a Spring-based programming model for MongoDB. Simplifies document operations, offers repository support, geo-spatial queries, GridFS, and full-text search integration with Spring's template pattern.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-mongodb
    baseURL: http://localhost:8080
    tags:
      - Document Database
      - MongoDB
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/mongodb/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-mongodb
      - type: API Reference
        url: https://docs.spring.io/spring-data/mongodb/docs/current/api/
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-mongodb
  - aid: spring-data:spring-data-redis
    name: Spring Data Redis
    description: Easy configuration and access to Redis from Spring applications. Provides low-level and high-level abstractions for storing, reading, querying data. Supports both reactive and imperative programming models.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-redis
    baseURL: http://localhost:8080
    tags:
      - Cache
      - Key-Value Store
      - Pub/Sub
      - Redis
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/redis/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-redis
      - type: API Reference
        url: https://docs.spring.io/spring-data/redis/docs/current/api/
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-redis
  - aid: spring-data:spring-data-cassandra
    name: Spring Data Cassandra
    description: Provides Spring-based programming model and repository support for Apache Cassandra. Offers CassandraTemplate, repository abstraction, query derivation, and reactive programming support with Project Reactor.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-cassandra
    baseURL: http://localhost:8080
    tags:
      - Cassandra
      - Distributed Database
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/cassandra/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-cassandra
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-cassandra
  - aid: spring-data:spring-data-neo4j
    name: Spring Data Neo4j
    description: Spring-based programming model for Neo4j graph database. Provides repository support, object-graph mapping, Cypher query derivation, and reactive Neo4j integration with full Spring ecosystem compatibility.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-neo4j
    baseURL: http://localhost:8080
    tags:
      - Graph Database
      - Neo4j
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/neo4j/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-neo4j
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-neo4j
  - aid: spring-data:spring-data-elasticsearch
    name: Spring Data Elasticsearch
    description: Spring Data module for Elasticsearch search engine. Provides ElasticsearchTemplate, repository abstraction, index management, full-text search queries, and reactive Elasticsearch client support.
    image: https://spring.io/img/projects/spring-data.svg
    humanURL: https://spring.io/projects/spring-data-elasticsearch
    baseURL: http://localhost:8080
    tags:
      - Elasticsearch
      - Full-Text Search
      - Search Engine
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/elasticsearch/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-data-elasticsearch
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.data/spring-data-elasticsearch
common:
  - type: Website
    url: https://spring.io/projects/spring-data
  - type: Blog
    url: https://spring.io/blog/category/data
  - type: GitHub Organization
    url: https://github.com/spring-projects
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-data
  - type: License
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Maven Repository
    url: https://mvnrepository.com/search?q=spring-data
  - type: Releases
    url: https://github.com/spring-projects/spring-data-commons/releases
  - type: Issues
    url: https://github.com/spring-projects/spring-data-commons/issues
  - type: Changelog
    url: https://github.com/spring-projects/spring-data-commons/blob/main/CHANGELOG.adoc
maintainers:
  - FN: Spring Team
    email: spring-data@pivotal.io
    X-twitter: springcentral
    X-github: spring-projects
include: []
---
