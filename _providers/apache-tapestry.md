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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Tapestry Component API provides Java annotations and interfaces for building reusable web components. Components are defined by a Java class and an HTML template file. The API includes @Component,
  name: Apache Tapestry Component API
  slug: apache-tapestry-component-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/tapestry-5/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/tapestry-5/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tapestry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tapestry-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tapestry-5
- group: docs
  title: ''
  type: Documentation
  url: https://tapestry.apache.org/documentation.html
- group: start
  title: ''
  type: Portal
  url: https://tapestry.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://tapestry.apache.org/getting-started.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/tapestry-5/releases
- group: operate
  title: ''
  type: Support
  url: https://tapestry.apache.org/community.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache Tapestry is a component-oriented framework for creating highly scalable web applications in Java. It provides a component-based development model with live class reloading, built-in Ajax support, type-safe URL generation, strong convention-over-configuration principles, and deep IDE integration. Tapestry applications are highly testable and work well with dependency injection via Tapestry IoC. It is maintained by the Apache Software Foundation.
features:
- description: Hot class reloading during development without server restart for faster iteration.
  name: Live Class Reloading
- description: Pure component-based development with isolated component state and event handling.
  name: Component Model
- description: Built-in inversion of control container with service binding and decoration.
  name: Tapestry IoC
- description: Built-in Zone components for partial page updates and Ajax event handling.
  name: Ajax Support
- description: Type-safe URL generation with automatic parameter encoding and SEO-friendly URLs.
  name: Type-Safe URLs
- description: Automatic asset minification, versioning, and CDN support for JavaScript and CSS.
  name: Asset Pipeline
finops:
- name: Apache Tapestry Finops
  service_category: API
  slug: apache-tapestry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-tapestry.png
integrations:
- description: Spring IoC integration for service injection into Tapestry pages and components.
  name: Spring Framework
- description: Hibernate ORM integration for database access from Tapestry pages.
  name: Hibernate
- description: JPA integration module for entity management in Tapestry applications.
  name: JPA
layout: provider
modified: '2026-04-19'
name: Apache Tapestry
nav: Providers
network: true
overview: 'Apache Tapestry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Component-Based, Java, Web Applications, Web Framework, and Open Source.


  Apache Tapestry''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 7 more developer resources.'
plans:
- name: Apache Tapestry Plans Pricing
  plan_count: 3
  slug: apache-tapestry-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 5
  name: Apache Tapestry Rate Limits
  slug: apache-tapestry-rate-limits
score:
  band: emerging
  composite: 22.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tapestry/refs/heads/main/screenshots/apache-tapestry-2026-06-20T172151.png
security:
- kind: domain-security
  name: Apache Tapestry Domain Security
  slug: apache-tapestry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tapestry Vulnerability Disclosure
  slug: apache-tapestry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tapestry
tags:
- Component-Based
- Java
- Web Applications
- Web Framework
- Open Source
- Ajax
use_cases:
- description: Large-scale enterprise applications with reusable component libraries.
  name: Enterprise Java Web Applications
- description: Complex data entry applications with server-side validation and type coercion.
  name: Form-Heavy Applications
- description: Ajax-driven UIs with partial page updates via Tapestry Zone components.
  name: Single-Page Application Backends
website: https://tapestry.apache.org/
---
