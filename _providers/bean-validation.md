---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The Jakarta Bean Validation 3.1 specification defines the constraint model, annotation processor, Validator API, method validation, group sequences, cascaded validation, constraint composition, and th
  name: Jakarta Bean Validation Specification 3.1
  slug: specification
- description: Hibernate Validator is the reference implementation of Jakarta Bean Validation. Version 9.1.0.Final implements the Jakarta Validation 3.1 specification. It provides the Validator, ValidatorFactory, Co
  name: Hibernate Validator
  slug: hibernate-validator
- description: The Jakarta Validation API JAR provides the interfaces, annotations, and exception types that constitute the Bean Validation specification contract. Constraint annotations (@NotNull, @Size, @Min, @Max
  name: Jakarta Validation API
  slug: jakarta-validation-api
artifact_total: 22
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jakartaee/validation/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jakartaee/validation/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jakartaee/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jakartaee/validation/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/jakartaee/validation/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bean-validation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beanvalidation.org/
- group: company
  title: ''
  type: Blog
  url: https://beanvalidation.org/news/news.atom
- group: docs
  title: ''
  type: Documentation
  url: https://beanvalidation.org/2.0/spec/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee
- group: design
  title: ''
  type: Versioning
  url: https://beanvalidation.org/news/
created: '2025-01-01'
description: Jakarta Bean Validation (formerly Java Bean Validation / JSR 380) is a Java specification providing a standardized constraint model and API for validating Java beans using annotations. It defines built-in constraints (@NotNull, @Size, @Min, @Max, @Pattern, @Email, etc.), a Validator API, constraint inheritance, and method/constructor parameter validation. The current stable release is Jakarta Validation 3.1. Hibernate Validator is the reference implementation. The specification is governed by the Jakarta EE Working Group under the Eclipse Foundation.
features:
- description: Define validation constraints on Java beans using annotations such as @NotNull, @Size, @Min, @Max, @Pattern, @Email, and @Past.
  name: Annotation-Based Constraints
- description: Validate method and constructor parameters and return values using constraint annotations on method signatures.
  name: Method Validation
- description: Compose multiple constraints together using @Constraint and meta-annotations to create custom reusable constraint annotations.
  name: Constraint Composition
- description: Define validation groups and group sequences for ordered, conditional validation scenarios.
  name: Group Sequences
- description: Trigger validation of nested objects using @Valid annotation for graph-level constraint validation.
  name: Cascaded Validation
- description: Build and configure validators programmatically using the Validator and ValidatorFactory APIs without annotations.
  name: Programmatic API
finops:
- name: Bean Validation Finops
  service_category: API
  slug: bean-validation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bean-validation.png
integrations:
- description: Spring integrates Jakarta Bean Validation for controller method argument validation and service layer validation.
  name: Spring Framework
- description: JPA providers call the Validator API before persisting entities to enforce database-layer constraint validation.
  name: Jakarta Persistence (JPA)
- description: Quarkus uses Hibernate Validator as its Bean Validation implementation with zero-config support in native images.
  name: Quarkus
- description: Jakarta Faces integrates Bean Validation for automatic form field validation in web applications.
  name: Jakarta Faces (JSF)
- description: Micronaut Framework uses Bean Validation for controller parameter and return value validation.
  name: Micronaut
layout: provider
modified: '2026-04-19'
name: Bean Validation
nav: Providers
network: true
overview: 'Bean Validation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bean Validation, Data Quality, Java, Validation, and Jakarta EE.


  Bean Validation''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Bean Validation Plans Pricing
  plan_count: 3
  slug: bean-validation-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Bean Validation Rate Limits
  slug: bean-validation-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bean-validation/refs/heads/main/screenshots/bean-validation-2026-06-20T173105.png
security:
- kind: domain-security
  name: Bean Validation Domain Security
  slug: bean-validation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bean-validation
tags:
- Bean Validation
- Data Quality
- Java
- Validation
- Jakarta EE
- Constraints
use_cases:
- description: Validate request body and query parameters in JAX-RS and Spring REST controllers using Bean Validation annotations.
  name: REST API Input Validation
- description: Validate user-submitted form data in Jakarta Faces, Spring MVC, and other web frameworks.
  name: Form Validation
- description: Enforce business rules and data integrity constraints on JPA entity classes and domain objects.
  name: Domain Model Validation
- description: Validate inter-service request and response payloads to enforce API contracts in microservices architectures.
  name: Microservices Contract Validation
website: https://beanvalidation.org/
---
