---
aid: spring-boot-admin-console
url: https://raw.githubusercontent.com/api-evangelist/spring-boot-admin-console/refs/heads/main/apis.yml
apis:
- name: Spring Boot Admin Server API
  description: The main API for the Spring Boot Admin server that provides endpoints for registering applications, retrieving application information, and monitoring status.
  baseURL: http://localhost:8080
  humanURL: https://codecentric.github.io/spring-boot-admin/current/
  properties:
  - type: Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/
  - type: OpenAPI
    url: http://localhost:8080/v3/api-docs
  tags:
  - Administration
  - Monitoring
  - Server
- name: Applications API
  description: Manage and retrieve information about registered Spring Boot applications.
  baseURL: http://localhost:8080/applications
  properties:
  - type: Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/#_applications
  endpoints:
  - path: /applications
    methods:
    - GET
    - POST
    description: List all registered applications or register a new application
  - path: /applications/{id}
    methods:
    - GET
    - DELETE
    description: Get or unregister a specific application by ID
  - path: /applications/{id}/actuator
    methods:
    - GET
    description: Get actuator endpoints for a specific application
  tags:
  - Applications
  - Registration
- name: Instances API
  description: Retrieve information about application instances.
  baseURL: http://localhost:8080/instances
  properties:
  - type: Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/#_instances
  endpoints:
  - path: /instances
    methods:
    - GET
    description: List all registered application instances
  - path: /instances/{id}
    methods:
    - GET
    - DELETE
    description: Get or unregister a specific instance
  - path: /instances/{id}/actuator/**
    methods:
    - GET
    - POST
    description: Proxy requests to actuator endpoints of the instance
  - path: /instances/{id}/actuator/health
    methods:
    - GET
    description: Get health information of the instance
  - path: /instances/{id}/actuator/info
    methods:
    - GET
    description: Get info about the instance
  - path: /instances/{id}/actuator/metrics
    methods:
    - GET
    description: Get metrics from the instance
  - path: /instances/{id}/actuator/env
    methods:
    - GET
    description: Get environment properties of the instance
  - path: /instances/{id}/actuator/loggers
    methods:
    - GET
    - POST
    description: View and modify logger configurations
  tags:
  - Actuator
  - Instances
  - Monitoring
- name: Events API
  description: Retrieve application lifecycle and state change events.
  baseURL: http://localhost:8080/instances/events
  properties:
  - type: Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/#_event-store
  endpoints:
  - path: /instances/events
    methods:
    - GET
    description: Stream of events (SSE - Server-Sent Events)
  tags:
  - Events
  - Notifications
- name: Notifications API
  description: Configure and manage notification channels for application events.
  baseURL: http://localhost:8080
  properties:
  - type: Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/#_notifications
  tags:
  - Alerts
  - Notifications
name: Spring Boot Admin Console
tags:
- Actuator
- Administration
- Java
- Microservices
- Monitoring
- Spring Boot
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Spring Boot Admin is a community project to manage and monitor Spring Boot applications. It provides a web-based UI to visualize and interact with Spring Boot Actuator endpoints.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

