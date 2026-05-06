---
name: Spring Boot Admin Console
description: Spring Boot Admin is a community project by codecentric AG that provides a web-based administration UI for managing and monitoring Spring Boot applications. It visualizes Spring Boot Actuator endpoints in a graphical interface and provides application registration, health monitoring, log level management, metric graphs, instance lifecycle event tracking, and notification integrations (email, Slack, PagerDuty, OpsGenie, Hipchat, Teams, Telegram).
url: https://github.com/codecentric/spring-boot-admin
image: https://raw.githubusercontent.com/codecentric/spring-boot-admin/master/spring-boot-admin-docs/src/site/resources/images/spring-boot-admin-logo.png
type: opensource
tags:
  - Actuator
  - Administration
  - Java
  - Microservices
  - Monitoring
  - Spring Boot
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.18'
apis:
  - name: Spring Boot Admin Server API
    description: REST API for the Spring Boot Admin server that manages application registration, retrieves application and instance information, proxies Actuator endpoints, and streams lifecycle events via Server-Sent Events.
    baseURL: http://localhost:8080
    humanURL: https://codecentric.github.io/spring-boot-admin/current/
    tags:
      - Administration
      - Monitoring
      - Server
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/
      - type: GitHub Repository
        url: https://github.com/codecentric/spring-boot-admin
      - type: OpenAPI
        url: openapi/spring-boot-admin-console-openapi.yml
      - type: Spectral Rules
        url: rules/spring-boot-admin-console-rules.yml
      - type: Maven Central
        url: https://mvnrepository.com/artifact/de.codecentric/spring-boot-admin-server
      - type: Release Notes
        url: https://github.com/codecentric/spring-boot-admin/releases
  - name: Applications API
    description: Manage registered Spring Boot applications. Applications are logical groupings of instances sharing the same name and management URL base.
    baseURL: http://localhost:8080/applications
    humanURL: https://codecentric.github.io/spring-boot-admin/current/#_applications
    tags:
      - Applications
      - Registration
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/#_applications
  - name: Instances API
    description: Manage individual application instances. Each instance represents a running Spring Boot application registered with the Admin server. Supports health monitoring, Actuator endpoint proxying, and deregistration.
    baseURL: http://localhost:8080/instances
    humanURL: https://codecentric.github.io/spring-boot-admin/current/#_instances
    tags:
      - Actuator
      - Instances
      - Monitoring
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/#_instances
  - name: Events API
    description: Lifecycle event stream for application instances using Server-Sent Events (SSE). Events include status changes, registration, deregistration, and info updates.
    baseURL: http://localhost:8080/instances/events
    humanURL: https://codecentric.github.io/spring-boot-admin/current/#_event-store
    tags:
      - Events
      - Notifications
      - SSE
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/#_event-store
  - name: Notifications API
    description: Configure and trigger notification channels for application lifecycle events. Supports email, Slack, PagerDuty, OpsGenie, Microsoft Teams, Telegram, and custom webhook notifications.
    baseURL: http://localhost:8080
    humanURL: https://codecentric.github.io/spring-boot-admin/current/#_notifications
    tags:
      - Alerts
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/#_notifications
maintainers:
  - name: codecentric AG
    url: https://www.codecentric.de/
    email: info@codecentric.de
common:
  - type: GitHub Repository
    url: https://github.com/codecentric/spring-boot-admin
  - type: Issue Tracker
    url: https://github.com/codecentric/spring-boot-admin/issues
  - type: Getting Started Guide
    url: https://codecentric.github.io/spring-boot-admin/current/#getting-started
  - type: Reference Documentation
    url: https://codecentric.github.io/spring-boot-admin/current/
  - type: Maven Central
    url: https://mvnrepository.com/artifact/de.codecentric/spring-boot-admin
  - type: License
    url: https://github.com/codecentric/spring-boot-admin/blob/master/LICENSE
  - type: Community
    url: https://gitter.im/codecentric/spring-boot-admin
---
