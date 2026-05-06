---
aid: spring-cloud-stream
name: Spring Cloud Stream
description: Spring Cloud Stream is a framework for building event-driven microservices connected with shared messaging systems. It provides a flexible programming model built on established Spring idioms and best practices, including support for persistent pub/sub semantics, consumer groups, and stateful partitions with Apache Kafka and RabbitMQ binders.
image: https://spring.io/img/projects/spring-cloud.svg
url: https://spring.io/projects/spring-cloud-stream
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Apache Kafka
  - AsyncAPI
  - Event-Driven
  - Java
  - Messaging
  - Microservices
  - RabbitMQ
  - Spring Framework
  - Stream Processing
apis:
  - aid: spring-cloud-stream:spring-cloud-stream-core
    name: Spring Cloud Stream Core API
    description: Core programmatic API for building message-driven microservice applications. Provides functional programming model with java.util.function.Function, Consumer and Supplier bindings, binding lifecycle management, and integration with Spring Integration for message transformation and routing.
    humanURL: https://spring.io/projects/spring-cloud-stream
    baseURL: https://repo.spring.io/milestone/org/springframework/cloud/spring-cloud-stream
    tags:
      - Bindings
      - Consumer Groups
      - Event-Driven
      - Functional Programming
      - Messaging
      - Microservices
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-stream/docs/current/reference/html/
      - type: API Documentation
        url: https://docs.spring.io/spring-cloud-stream/docs/current/api/
      - type: Getting Started
        url: https://spring.io/projects/spring-cloud-stream#learn
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-stream
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-stream
      - type: Samples
        url: https://github.com/spring-cloud/spring-cloud-stream-samples
      - type: Releases
        url: https://github.com/spring-cloud/spring-cloud-stream/releases
      - type: Issues
        url: https://github.com/spring-cloud/spring-cloud-stream/issues
      - type: JSONSchema
        url: json-schema/spring-cloud-stream-binding-schema.json
      - type: JSONStructure
        url: json-structure/spring-cloud-stream-binding-structure.json
      - type: JSONLDContext
        url: json-ld/spring-cloud-stream-context.jsonld
  - aid: spring-cloud-stream:spring-cloud-stream-kafka-binder
    name: Spring Cloud Stream Kafka Binder
    description: Apache Kafka binder for Spring Cloud Stream providing Kafka producer and consumer binding configuration, Kafka Streams support, partitioning, transaction management, error handling, and dead-letter queues.
    humanURL: https://docs.spring.io/spring-cloud-stream-binder-kafka/docs/current/reference/html/
    baseURL: https://kafka.apache.org
    tags:
      - Apache Kafka
      - Binder
      - Event Streaming
      - Kafka Streams
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-stream-binder-kafka/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-stream-binder-kafka
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-stream-binder-kafka
  - aid: spring-cloud-stream:spring-cloud-stream-rabbitmq-binder
    name: Spring Cloud Stream RabbitMQ Binder
    description: RabbitMQ binder for Spring Cloud Stream providing AMQP-based messaging with support for exchanges, queues, routing keys, dead-letter exchanges, consumer groups, and AMQP transaction management.
    humanURL: https://docs.spring.io/spring-cloud-stream-binder-rabbit/docs/current/reference/html/
    baseURL: https://www.rabbitmq.com
    tags:
      - AMQP
      - Binder
      - Messaging
      - RabbitMQ
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-stream-binder-rabbit/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-stream-binder-rabbit
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-stream-binder-rabbit
common:
  - type: Website
    url: https://spring.io/projects/spring-cloud-stream
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-stream/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-stream
  - type: GitHub Organization
    url: https://github.com/spring-cloud
  - type: Blog
    url: https://spring.io/blog/category/cloud
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-cloud-stream
  - type: Support
    url: https://spring.io/support
  - type: Vocabulary
    url: vocabulary/spring-cloud-stream-vocabulary.yml
maintainers:
  - FN: VMware Tanzu (Spring Team)
    email: spring-cloud@vmware.com
    url: https://spring.io/team
---
