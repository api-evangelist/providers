---
aid: jboss
name: JBoss
description: JBoss is a division of Red Hat providing open source middleware and application server technologies for enterprise Java workloads. The JBoss product portfolio includes JBoss EAP (Enterprise Application Platform), the WildFly community application server, JBoss Data Grid (Red Hat Data Grid), Keycloak identity and access management, and JBoss Fuse integration platform built on Apache Camel. These projects power Jakarta EE deployments, single sign-on, distributed caching, and microservices integration in enterprise environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Server
  - Cloud Native
  - Enterprise
  - Jakarta EE
  - Java EE
  - Microservices
  - Middleware
  - Open Source
  - Red Hat
url: https://raw.githubusercontent.com/api-evangelist/jboss/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jboss:jboss-eap-management-api
    name: JBoss EAP Management API
    description: RESTful management API for JBoss Enterprise Application Platform (EAP) administration and monitoring of server configuration, deployments, and runtime state.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform
    tags:
      - Application Server
      - Management
      - Middleware
    properties:
      - type: Documentation
        url: https://docs.jboss.org/author/display/WFLY/Management+API+reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/wildfly/wildfly/main/docs/src/main/asciidoc/_admin-guide/management-api/OpenAPI.yaml
      - type: Authentication
        url: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.4/html/configuration_guide/management_api_reference
  - aid: jboss:wildfly-rest-api
    name: WildFly REST API
    description: RESTful interface for WildFly (the community version of JBoss EAP) server management, deployments, and runtime configuration.
    humanURL: https://wildfly.org
    tags:
      - Application Server
      - Management
      - WildFly
    properties:
      - type: Documentation
        url: https://docs.wildfly.org/
      - type: GitHub
        url: https://github.com/wildfly/wildfly
      - type: Reference
        url: https://docs.wildfly.org/management-api/
  - aid: jboss:jboss-data-grid-rest-api
    name: JBoss Data Grid REST API
    description: REST API for distributed in-memory caching with JBoss Data Grid (Red Hat Data Grid), based on the Infinispan project.
    humanURL: https://access.redhat.com/products/red-hat-data-grid
    tags:
      - Cache
      - Data Grid
      - Distributed Systems
      - In-Memory
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_data_grid/8.4/html/data_grid_rest_api
      - type: Reference
        url: https://infinispan.org/docs/stable/titles/rest/rest.html
  - aid: jboss:keycloak-admin-rest-api
    name: Keycloak Admin REST API
    description: Administration REST API for Keycloak identity and access management, supporting OAuth2, OpenID Connect, and SAML for SSO scenarios.
    humanURL: https://www.keycloak.org
    tags:
      - Authentication
      - Authorization
      - Identity Management
      - OAuth2
      - OpenID Connect
      - SSO
    properties:
      - type: Documentation
        url: https://www.keycloak.org/docs/latest/server_development/#admin-rest-api
      - type: OpenAPI
        url: https://www.keycloak.org/docs-api/latest/rest-api/openapi.json
      - type: GitHub
        url: https://github.com/keycloak/keycloak
  - aid: jboss:jboss-fuse-rest-dsl
    name: JBoss Fuse REST DSL
    description: REST DSL for Apache Camel integration in JBoss Fuse, enabling definition of REST endpoints and routes for enterprise integration patterns.
    humanURL: https://access.redhat.com/products/red-hat-fuse
    tags:
      - Camel
      - ESB
      - Integration
      - Microservices
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_fuse/7.11/html/apache_camel_development_guide/basicprinciples-restdsl
      - type: Reference
        url: https://camel.apache.org/components/latest/rest-api-component.html
common:
  - type: Portal
    url: https://developers.redhat.com/products/eap/overview
  - type: Getting Started
    url: https://www.jboss.org/get-started/
  - type: Blog
    url: https://www.jboss.org/posts/
  - type: GitHub Organization
    url: https://github.com/jbossas
  - type: Support
    url: https://access.redhat.com/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
