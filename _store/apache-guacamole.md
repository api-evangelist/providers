---
aid: apache-guacamole
name: Apache Guacamole
description: Apache Guacamole is a clientless remote desktop gateway that supports standard protocols like VNC, RDP, and SSH. It requires no plugins or client software and provides access to remote desktops through a web browser with a comprehensive REST API for connection, user, and session management.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Open Source
  - RDP
  - Remote Access
  - Remote Desktop
  - SSH
  - VNC
  - Web Gateway
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-guacamole/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-guacamole:apache-guacamole-rest-api
    name: Apache Guacamole REST API
    description: REST API for managing connections, users, groups, and active sessions in Apache Guacamole remote desktop gateway, with token-based authentication and per-data-source resource management.
    humanURL: https://guacamole.apache.org/doc/gug/guacamole-rest-api.html
    baseURL: http://localhost:8080
    tags:
      - Authentication
      - Connections
      - Remote Desktop
      - REST
      - Users
    properties:
      - type: Documentation
        url: https://guacamole.apache.org/doc/gug/guacamole-rest-api.html
      - type: OpenAPI
        url: openapi/apache-guacamole-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/guacamole-rest-auth-token-schema.json
      - type: JSON-LD
        url: json-ld/apache-guacamole-rest-context.jsonld
  - aid: apache-guacamole:apache-guacamole-javascript-api
    name: Apache Guacamole JavaScript Client API
    description: JavaScript client library for embedding the Guacamole remote desktop client in web applications, with APIs for protocol tunneling, display rendering, and user input handling.
    humanURL: https://guacamole.apache.org/doc/gug/writing-you-own-guacamole-app.html
    tags:
      - JavaScript
      - Remote Desktop
      - SDK
    properties:
      - type: Documentation
        url: https://guacamole.apache.org/doc/gug/writing-you-own-guacamole-app.html
common:
  - type: Documentation
    url: https://guacamole.apache.org/doc/gug/
  - type: GettingStarted
    url: https://guacamole.apache.org/doc/gug/users-guide.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/guacamole-client
  - type: SpectralRules
    url: rules/apache-guacamole-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-guacamole-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/guacamole-remote-access.yaml
  - type: Features
    data:
      - name: Clientless Remote Desktop
        description: Access remote desktops through any HTML5 web browser with no client software or plugins required.
      - name: Multi-Protocol Support
        description: Supports VNC, RDP, SSH, and Telnet protocols through a unified web gateway.
      - name: Token-Based Authentication
        description: Stateless REST API authentication using time-limited tokens from the /api/tokens endpoint.
      - name: Connection Management
        description: REST API for creating, updating, and organizing remote desktop connections and connection groups.
      - name: User and Group Management
        description: Fine-grained user and group permissions for controlling access to connections and administrative functions.
      - name: Active Session Monitoring
        description: Monitor and terminate active remote desktop sessions through the REST API.
      - name: Connection History
        description: Audit log of all remote desktop sessions with timestamps and user attribution.
      - name: Extension API
        description: Java extension API for implementing custom authentication providers, event listeners, and protocol extensions.
  - type: UseCases
    data:
      - name: Remote Desktop Access
        description: Provide browser-based access to Linux and Windows desktops for remote workers.
      - name: Cloud Server Management
        description: Access cloud VMs and servers through SSH and RDP via browser without installing VPN or client software.
      - name: Secure Bastion Host
        description: Use Guacamole as a protocol-proxying bastion host to isolate internal systems from direct network access.
      - name: Development Environment Access
        description: Provide developers with browser-based access to containerized or virtualized development environments.
      - name: IT Support Tooling
        description: Enable IT helpdesk teams to access and troubleshoot user desktops through the browser.
  - type: Integrations
    data:
      - name: Apache Tomcat
        description: Runs as a Java web application on Apache Tomcat or any Java Servlet container.
      - name: LDAP / Active Directory
        description: LDAP extension for authenticating users against directory services like Active Directory.
      - name: TOTP / Duo MFA
        description: Multi-factor authentication extensions supporting TOTP apps and Duo Security.
      - name: MySQL / PostgreSQL
        description: Database authentication extensions for storing connections and users in relational databases.
      - name: Kubernetes
        description: Guacamole can be deployed on Kubernetes with the guacamole-client Docker image.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
