---
aid: bean-validation
name: Bean Validation
description: Jakarta Bean Validation (formerly Java Bean Validation / JSR 380) is a Java specification providing a standardized constraint model and API for validating Java beans using annotations. It defines built-in constraints (@NotNull, @Size, @Min, @Max, @Pattern, @Email, etc.), a Validator API, constraint inheritance, and method/constructor parameter validation. The current stable release is Jakarta Validation 3.1. Hibernate Validator is the reference implementation. The specification is governed by the Jakarta EE Working Group under the Eclipse Foundation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bean Validation
  - Data Quality
  - Java
  - Validation
  - Jakarta EE
  - Constraints
url: https://raw.githubusercontent.com/api-evangelist/bean-validation/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: bean-validation:specification
    name: Jakarta Bean Validation Specification 3.1
    description: The Jakarta Bean Validation 3.1 specification defines the constraint model, annotation processor, Validator API, method validation, group sequences, cascaded validation, constraint composition, and the metadata API for introspecting validation constraints on Java classes, fields, methods, and constructors.
    humanURL: https://beanvalidation.org/3.1/
    tags:
      - Bean Validation
      - Java
      - Jakarta EE
      - Specification
    properties:
      - type: Documentation
        url: https://beanvalidation.org/3.1/
      - type: Specification
        url: https://jakarta.ee/specifications/bean-validation/3.1/
      - type: GitHubRepository
        url: https://github.com/jakartaee/validation
  - aid: bean-validation:hibernate-validator
    name: Hibernate Validator
    description: Hibernate Validator is the reference implementation of Jakarta Bean Validation. Version 9.1.0.Final implements the Jakarta Validation 3.1 specification. It provides the Validator, ValidatorFactory, ConstraintViolation APIs, additional built-in constraints beyond the spec, programmatic constraint definition, and message interpolation. Available via Maven Central and published under Apache 2.0.
    humanURL: https://hibernate.org/validator/
    tags:
      - Bean Validation
      - Java
      - Reference Implementation
      - Hibernate
    properties:
      - type: Documentation
        url: https://docs.jboss.org/hibernate/stable/validator/reference/en-US/html_single/
      - type: GettingStarted
        url: https://hibernate.org/validator/documentation/getting-started/
      - type: GitHubRepository
        url: https://github.com/hibernate/hibernate-validator
      - type: SDK
        url: https://mvnrepository.com/artifact/org.hibernate.validator/hibernate-validator
        title: Maven Central
  - aid: bean-validation:jakarta-validation-api
    name: Jakarta Validation API
    description: The Jakarta Validation API JAR provides the interfaces, annotations, and exception types that constitute the Bean Validation specification contract. Constraint annotations (@NotNull, @Size, @Min, @Max, @Pattern, @Email, @Future, @Past, @Positive, @Negative, etc.), Validator, ValidatorFactory, ConstraintViolation, and Path types are all defined in the API. Available on Maven Central.
    humanURL: https://jakarta.ee/specifications/bean-validation/3.1/
    tags:
      - Bean Validation
      - Java
      - API
      - Jakarta EE
    properties:
      - type: Specification
        url: https://jakarta.ee/specifications/bean-validation/3.1/
      - type: SDK
        url: https://mvnrepository.com/artifact/jakarta.validation/jakarta.validation-api
        title: Maven Central
common:
  - type: Website
    url: https://beanvalidation.org/
  - type: Documentation
    url: https://beanvalidation.org/2.0/spec/
  - type: GitHubOrganization
    url: https://github.com/jakartaee
  - type: Versioning
    url: https://beanvalidation.org/news/
  - type: Features
    data:
      - name: Annotation-Based Constraints
        description: Define validation constraints on Java beans using annotations such as @NotNull, @Size, @Min, @Max, @Pattern, @Email, and @Past.
      - name: Method Validation
        description: Validate method and constructor parameters and return values using constraint annotations on method signatures.
      - name: Constraint Composition
        description: Compose multiple constraints together using @Constraint and meta-annotations to create custom reusable constraint annotations.
      - name: Group Sequences
        description: Define validation groups and group sequences for ordered, conditional validation scenarios.
      - name: Cascaded Validation
        description: Trigger validation of nested objects using @Valid annotation for graph-level constraint validation.
      - name: Programmatic API
        description: Build and configure validators programmatically using the Validator and ValidatorFactory APIs without annotations.
  - type: UseCases
    data:
      - name: REST API Input Validation
        description: Validate request body and query parameters in JAX-RS and Spring REST controllers using Bean Validation annotations.
      - name: Form Validation
        description: Validate user-submitted form data in Jakarta Faces, Spring MVC, and other web frameworks.
      - name: Domain Model Validation
        description: Enforce business rules and data integrity constraints on JPA entity classes and domain objects.
      - name: Microservices Contract Validation
        description: Validate inter-service request and response payloads to enforce API contracts in microservices architectures.
  - type: Integrations
    data:
      - name: Spring Framework
        description: Spring integrates Jakarta Bean Validation for controller method argument validation and service layer validation.
      - name: Jakarta Persistence (JPA)
        description: JPA providers call the Validator API before persisting entities to enforce database-layer constraint validation.
      - name: Quarkus
        description: Quarkus uses Hibernate Validator as its Bean Validation implementation with zero-config support in native images.
      - name: Jakarta Faces (JSF)
        description: Jakarta Faces integrates Bean Validation for automatic form field validation in web applications.
      - name: Micronaut
        description: Micronaut Framework uses Bean Validation for controller parameter and return value validation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
