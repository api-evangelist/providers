---
aid: apache-shiro
name: Apache Shiro
description: Apache Shiro is a powerful and easy-to-use Java security framework that performs authentication, authorization, cryptography, and session management. It provides a clean API for securing applications from the smallest mobile applications to the largest enterprise systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Cryptography
  - Java
  - Security
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-shiro/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-shiro:apache-shiro
    name: Apache Shiro
    description: Shiro provides a Java API for authentication (login/logout), authorization (access control), cryptography (hashing/encryption), and session management, with support for web applications, REST APIs, and standalone applications.
    humanURL: https://shiro.apache.org/documentation.html
    tags:
      - Authentication
      - Authorization
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://shiro.apache.org/documentation.html
      - type: OpenAPI
        url: openapi/apache-shiro-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/shiro
  - type: Documentation
    url: https://shiro.apache.org/
  - type: SpectralRules
    url: rules/apache-shiro-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-shiro-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shiro-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-shiro-context.jsonld
  - type: Features
    data:
      - name: Authentication
        description: Pluggable authentication with username/password, remember-me, and token support
      - name: Authorization
        description: Role-based and permission-based access control with wildcard permissions
      - name: Session Management
        description: Native session management independent of HTTP containers
      - name: Cryptography
        description: Password hashing with salt, bcrypt, Argon2, and SHA-256
      - name: Multiple Realms
        description: JDBC, LDAP, properties file, and custom realm support
      - name: Web Integration
        description: Filter-based web application security with URL pattern matching
      - name: Annotations
        description: AOP and annotation-based security for method-level authorization
  - type: UseCases
    data:
      - name: Web Application Security
        description: Secure Java web applications with authentication and URL-based access control
      - name: REST API Security
        description: Protect REST APIs with token authentication and permission checks
      - name: Microservice Auth
        description: Stateless JWT authentication for microservice architectures
      - name: Admin Portal Security
        description: Role-based admin interface with fine-grained permissions
  - type: Integrations
    data:
      - name: Spring Framework
        description: Shiro Spring integration for bean-level security
      - name: Jakarta EE
        description: Java EE web filter integration for servlet containers
      - name: LDAP/Active Directory
        description: LDAP realm for enterprise user directory authentication
      - name: JDBC
        description: Database-backed realm for user and permission storage
      - name: Hazelcast
        description: Distributed session management with Hazelcast
---
