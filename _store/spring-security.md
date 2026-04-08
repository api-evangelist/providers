---
aid: spring-security
url: https://raw.githubusercontent.com/api-evangelist/spring-security/refs/heads/main/apis.yml
apis:
- name: Spring Security Core API
  description: Core security features including authentication and authorization.
  baseURL: https://docs.spring.io/spring-security/site/docs/current/api/
  humanURL: https://spring.io/projects/spring-security
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/
  - type: API Documentation
    url: https://docs.spring.io/spring-security/site/docs/current/api/
  - type: Getting Started
    url: https://spring.io/guides/gs/securing-web/
  - type: GitHub Repository
    url: https://github.com/spring-projects/spring-security
  - type: Release Notes
    url: https://github.com/spring-projects/spring-security/releases
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.security
  tags:
  - Authentication
  - Authorization
  - Core
  - Security
- name: Spring Security OAuth2
  description: OAuth 2.0 and OpenID Connect support for Spring Security.
  baseURL: https://docs.spring.io/spring-security/site/docs/current/api/
  humanURL: https://spring.io/projects/spring-security-oauth
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html
  - type: OAuth2 Client Documentation
    url: https://docs.spring.io/spring-security/reference/servlet/oauth2/client/index.html
  - type: OAuth2 Resource Server
    url: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html
  - type: Authorization Server
    url: https://spring.io/projects/spring-authorization-server
  tags:
  - Authorization
  - JWT
  - OAuth2
  - OpenID Connect
- name: Spring Security SAML
  description: SAML 2.0 Service Provider support.
  baseURL: https://docs.spring.io/spring-security-saml/docs/current/api/
  humanURL: https://docs.spring.io/spring-security/reference/servlet/saml2/index.html
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/servlet/saml2/index.html
  - type: SAML2 Login
    url: https://docs.spring.io/spring-security/reference/servlet/saml2/login/index.html
  - type: GitHub Repository
    url: https://github.com/spring-projects/spring-security
  tags:
  - Enterprise
  - Federation
  - SAML
  - SSO
- name: Spring Security LDAP
  description: LDAP authentication and authorization support.
  baseURL: https://docs.spring.io/spring-security/site/docs/current/api/
  humanURL: https://spring.io/projects/spring-security
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/ldap.html
  - type: Guide
    url: https://spring.io/guides/gs/authenticating-ldap/
  tags:
  - Authentication
  - Directory Services
  - Enterprise
  - LDAP
- name: Spring Security WebFlux
  description: Security for reactive Spring WebFlux applications.
  baseURL: https://docs.spring.io/spring-security/site/docs/current/api/
  humanURL: https://spring.io/projects/spring-security
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/reactive/index.html
  - type: Getting Started
    url: https://docs.spring.io/spring-security/reference/reactive/getting-started.html
  - type: OAuth2 WebFlux
    url: https://docs.spring.io/spring-security/reference/reactive/oauth2/index.html
  tags:
  - Async
  - Non-Blocking
  - Reactive
  - WebFlux
name: Spring Security
tags:
- Authentication
- Authorization
- Java
- JWT
- OAuth2
- SAML
- Security
- Spring Framework
type: Contract
image: https://spring.io/img/projects/spring-security.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Spring Security is a powerful and highly customizable authentication and access-control framework for Java applications. It is the de-facto standard for securing Spring-based applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

