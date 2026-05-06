---
aid: spring-security
name: Spring Security
description: Spring Security is a powerful and highly customizable authentication and access-control framework for Java applications. It is the de-facto standard for securing Spring-based applications, providing comprehensive security services including authentication, authorization, protection against common exploits (CSRF, session fixation, clickjacking), OAuth 2.0, OpenID Connect, SAML 2.0, LDAP, and WebFlux reactive security.
type: Index
image: https://spring.io/img/projects/spring-security.svg
url: https://spring.io/projects/spring-security
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Authentication
  - Authorization
  - Java
  - JWT
  - OAuth2
  - OpenID Connect
  - SAML
  - Security
  - Spring Framework
apis:
  - aid: spring-security:spring-security-oauth2
    name: Spring Security OAuth2 API
    description: OAuth 2.0 and OpenID Connect support for Spring Security. Provides client registration, authorization code flow, token endpoint, token refresh, PKCE support, and resource server JWT validation.
    humanURL: https://spring.io/projects/spring-security
    baseURL: http://localhost:8080
    tags:
      - Authorization Server
      - JWT
      - OAuth2
      - OpenID Connect
      - Token
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html
      - type: OAuth2 Client Documentation
        url: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html
      - type: OAuth2 Resource Server
        url: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html
      - type: Authorization Server
        url: https://spring.io/projects/spring-authorization-server
      - type: OpenAPI
        url: openapi/spring-security-oauth2-openapi.yml
  - aid: spring-security:spring-authorization-server
    name: Spring Authorization Server API
    description: Spring's implementation of an OAuth 2.1 and OpenID Connect 1.0 authorization server. Provides issuing access tokens, refresh tokens, and ID tokens with support for PKCE, token introspection, and authorization server metadata.
    humanURL: https://spring.io/projects/spring-authorization-server
    baseURL: http://localhost:9000
    tags:
      - Authorization Server
      - OAuth2
      - OpenID Connect
      - Token Issuance
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-authorization-server/docs/current/reference/html/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-authorization-server
      - type: Getting Started
        url: https://docs.spring.io/spring-authorization-server/docs/current/reference/html/getting-started.html
      - type: OpenAPI
        url: openapi/spring-authorization-server-openapi.yml
  - aid: spring-security:spring-security-core
    name: Spring Security Core
    description: Core security features for authentication and authorization. Provides UserDetailsService, password encoding, security context management, method security, and HTTP security configuration.
    humanURL: https://spring.io/projects/spring-security
    baseURL: https://docs.spring.io/spring-security/site/docs/current/api/
    tags:
      - Authentication
      - Authorization
      - Core
      - Method Security
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/
      - type: API Reference
        url: https://docs.spring.io/spring-security/site/docs/current/api/
      - type: Getting Started
        url: https://spring.io/guides/gs/securing-web/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-security
      - type: Release Notes
        url: https://github.com/spring-projects/spring-security/releases
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.security
  - aid: spring-security:spring-security-saml
    name: Spring Security SAML2
    description: SAML 2.0 Service Provider support for Spring Security. Enables SSO integration with SAML identity providers, handling authentication requests, assertions, and SLO (Single Logout).
    humanURL: https://docs.spring.io/spring-security/reference/servlet/saml2/index.html
    tags:
      - Enterprise SSO
      - Federation
      - SAML
      - Single Logout
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/servlet/saml2/index.html
      - type: SAML2 Login
        url: https://docs.spring.io/spring-security/reference/servlet/saml2/login/index.html
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-security
  - aid: spring-security:spring-security-ldap
    name: Spring Security LDAP
    description: LDAP authentication and authorization support for Spring Security. Supports LDAP bind authentication, password comparison, and user details loading from directory services.
    humanURL: https://spring.io/projects/spring-security
    tags:
      - Authentication
      - Directory Services
      - Enterprise
      - LDAP
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/ldap.html
      - type: Guide
        url: https://spring.io/guides/gs/authenticating-ldap/
  - aid: spring-security:spring-security-webflux
    name: Spring Security WebFlux
    description: Reactive security for Spring WebFlux applications. Provides non-blocking authentication, authorization, OAuth2 reactive client support, and CSRF protection for reactive web stacks.
    humanURL: https://spring.io/projects/spring-security
    tags:
      - Non-Blocking
      - Reactive
      - Security
      - WebFlux
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/reactive/index.html
      - type: Getting Started
        url: https://docs.spring.io/spring-security/reference/reactive/getting-started.html
      - type: OAuth2 WebFlux
        url: https://docs.spring.io/spring-security/reference/reactive/oauth2/index.html
maintainers:
  - FN: Spring Security Team
    email: spring-security@vmware.com
    url: https://spring.io/team
include:
  - name: Spring Framework
    url: https://spring.io/projects/spring-framework
  - name: Spring Boot
    url: https://spring.io/projects/spring-boot
  - name: Spring Authorization Server
    url: https://spring.io/projects/spring-authorization-server
common:
  - type: Blog
    url: https://spring.io/blog/category/security
  - type: Community
    url: https://stackoverflow.com/questions/tagged/spring-security
  - type: Twitter
    url: https://twitter.com/SpringSecurity
  - type: Issue Tracker
    url: https://github.com/spring-projects/spring-security/issues
  - type: Contributing Guide
    url: https://github.com/spring-projects/spring-security/blob/main/CONTRIBUTING.adoc
  - type: License
    url: https://github.com/spring-projects/spring-security/blob/main/LICENSE.txt
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.security
  - type: Changelog
    url: https://github.com/spring-projects/spring-security/releases
---
