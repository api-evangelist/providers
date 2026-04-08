---
aid: spring-data
url: https://raw.githubusercontent.com/api-evangelist/spring-data/refs/heads/main/apis.yml
apis:
- name: Spring Data REST
  description: Exports Spring Data repositories as hypermedia-driven RESTful resources.
  image: https://spring.io/img/projects/spring-data.svg
  humanUrl: https://spring.io/projects/spring-data-rest
  baseUrl: http://localhost:8080
  tags:
  - HATEOAS
  - Repository
  - REST
  properties:
  - type: X-documentation
    url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
  - type: X-github
    url: https://github.com/spring-projects/spring-data-rest
  - type: X-api-definition
    url: https://docs.spring.io/spring-data/rest/docs/current/api/
  contact:
  - FN: Spring Team
    email: spring-data@pivotal.io
    X-twitter: springcentral
- name: Spring Data JPA
  description: Simplifies the development of creating a JPA-based data access layer.
  image: https://spring.io/img/projects/spring-data.svg
  humanUrl: https://spring.io/projects/spring-data-jpa
  baseUrl: http://localhost:8080
  tags:
  - Database
  - Hibernate
  - JPA
  - Repository
  properties:
  - type: X-documentation
    url: https://docs.spring.io/spring-data/jpa/docs/current/reference/html/
  - type: X-github
    url: https://github.com/spring-projects/spring-data-jpa
  - type: X-api-definition
    url: https://docs.spring.io/spring-data/jpa/docs/current/api/
  contact:
  - FN: Spring Team
    email: spring-data@pivotal.io
    X-twitter: springcentral
- name: Spring Data MongoDB
  description: Spring-based programming model for MongoDB.
  image: https://spring.io/img/projects/spring-data.svg
  humanUrl: https://spring.io/projects/spring-data-mongodb
  baseUrl: http://localhost:8080
  tags:
  - Document Database
  - MongoDB
  - NoSQL
  properties:
  - type: X-documentation
    url: https://docs.spring.io/spring-data/mongodb/docs/current/reference/html/
  - type: X-github
    url: https://github.com/spring-projects/spring-data-mongodb
  - type: X-api-definition
    url: https://docs.spring.io/spring-data/mongodb/docs/current/api/
  contact:
  - FN: Spring Team
    email: spring-data@pivotal.io
    X-twitter: springcentral
- name: Spring Data Redis
  description: Easy configuration and access to Redis from Spring applications.
  image: https://spring.io/img/projects/spring-data.svg
  humanUrl: https://spring.io/projects/spring-data-redis
  baseUrl: http://localhost:8080
  tags:
  - Cache
  - Key-Value Store
  - Redis
  properties:
  - type: X-documentation
    url: https://docs.spring.io/spring-data/redis/docs/current/reference/html/
  - type: X-github
    url: https://github.com/spring-projects/spring-data-redis
  - type: X-api-definition
    url: https://docs.spring.io/spring-data/redis/docs/current/api/
  contact:
  - FN: Spring Team
    email: spring-data@pivotal.io
    X-twitter: springcentral
name: Spring Data
tags:
- Data Access
- Database
- JPA
- MongoDB
- ORM
- Redis
- REST
- Spring
type: Contract
image: https://spring.io/img/projects/spring-data.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Spring Data's mission is to provide a familiar and consistent, Spring-based programming model for data access while still retaining the special traits of the underlying data store.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

