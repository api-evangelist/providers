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
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: The core Thymeleaf template engine library providing HTML, XML, TEXT, JavaScript, and CSS template mode processing. Includes the Standard Dialect with th:text, th:each, th:if, th:unless, th:switch, th
  name: Thymeleaf Core
  slug: thymeleaf-core
- description: The Thymeleaf Spring integration module (thymeleaf-spring6) providing deep integration with Spring Framework including the SpringStandardDialect using Spring EL, SpringTemplateEngine auto-configuratio
  name: Thymeleaf Spring Integration
  slug: thymeleaf-spring-integration
- description: 'Additional Thymeleaf dialect extensions including the Java 8 Time dialect for date/time formatting, the Spring Security dialect for security tag support, and community-maintained dialects such as the '
  name: Thymeleaf Extras and Dialects
  slug: thymeleaf-extras
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thymeleaf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thymeleaf.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thymeleaf.org/doc/tutorials/3.1/usingthymeleaf.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thymeleaf
- group: other
  title: ''
  type: Maven
  url: https://mvnrepository.com/artifact/org.thymeleaf/thymeleaf
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/thymeleaf/thymeleaf/issues
- group: other
  title: ''
  type: Spring Boot Starter
  url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-schema/thymeleaf-template-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-structure/thymeleaf-template-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/json-ld/thymeleaf-context.jsonld
created: '2026-03-16'
description: Thymeleaf is a modern server-side Java template engine for both web and standalone environments, capable of processing HTML, XML, JavaScript, CSS, and plain text. Its primary goal is to bring elegant natural templates to development workflows — HTML pages that can be correctly displayed in browsers as static prototypes while also working as dynamic server-side templates. With over 3,000 GitHub stars, Thymeleaf 3.1 offers deep Spring Framework integration via the Spring Standard Dialect using Spring EL, extensive tool support for Eclipse and IntelliJ IDEA, and an extensible dialect system. It is widely used in Spring Boot web applications as the standard server-side rendering solution.
examples:
- key_count: 9
  name: Thymeleaf Spring Boot Example
  slug: thymeleaf-spring-boot-example
finops:
- name: Thymeleaf Finops
  service_category: API
  slug: thymeleaf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thymeleaf.png
json_schemas:
- name: Thymeleaf Template Configuration
  property_count: 2
  slug: thymeleaf-template
json_structures:
- name: Thymeleaf Template Structure
  property_count: 0
  slug: thymeleaf-template-structure
jsonld:
- class_count: 23
  name: Thymeleaf Context
  property_count: 18
  slug: thymeleaf-context
layout: provider
modified: '2026-05-03'
name: Thymeleaf
nav: Providers
network: true
overview: 'Thymeleaf publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HTML, Java, Open-Source, Server-Side Rendering, and Spring.


  The Thymeleaf catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Thymeleaf''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Thymeleaf Plans Pricing
  plan_count: 3
  slug: thymeleaf-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Thymeleaf Rate Limits
  slug: thymeleaf-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Thymeleaf API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: thymeleaf-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 14.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thymeleaf/refs/heads/main/screenshots/thymeleaf-2026-06-20T195323.png
security:
- kind: domain-security
  name: Thymeleaf Domain Security
  slug: thymeleaf-domain-security
  summary_line: TLSv1.3
slug: thymeleaf
tags:
- HTML
- Java
- Open-Source
- Server-Side Rendering
- Spring
- Spring Boot
- Template Engine
- Thymeleaf
- Web Development
website: https://www.thymeleaf.org/
---
