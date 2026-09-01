---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apache Struts Agentic Access
  operation_count: 7
  slug: apache-struts-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: The Struts REST Plugin provides a convention-based REST API framework for building RESTful services. It maps HTTP methods to action methods (GET→index/show, POST→create, PUT→update, DELETE→destroy) an
  name: Apache Struts REST Plugin
  slug: apache-struts-rest-plugin
- description: Generic RESTful resource exposed by the Struts REST plugin
  name: Apache Struts resource API
  slug: apache-struts-resource-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Struts REST Plugin resource API
  slug: open-apache-struts-resource-api
- collection_type: open
  name: Apache Struts REST Plugin
  slug: open-apache-struts
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/struts/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/struts/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/struts/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-struts-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-struts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-struts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-struts-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/struts
- group: docs
  title: ''
  type: Documentation
  url: https://struts.apache.org/documentation.html
- group: start
  title: ''
  type: Portal
  url: https://struts.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://struts.apache.org/getting-started/index.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/struts/releases
- group: operate
  title: ''
  type: Support
  url: https://struts.apache.org/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: FAQ
  url: https://struts.apache.org/faq.html
- group: company
  title: ''
  type: Blog
  url: https://struts.apache.org/announce.html
created: '2026-03-16'
description: Apache Struts is a free, open-source, MVC framework for creating elegant, modern Java web applications. It provides a clean separation between the model, view, and controller layers with a powerful convention-over-configuration approach, interceptor-based AOP support, type-safe configuration, and built-in REST plugin. Apache Struts is maintained by the Apache Software Foundation and is widely used in enterprise Java web development.
features:
- description: Zero-XML configuration with naming conventions for action and result mapping.
  name: Convention-Over-Configuration
- description: AOP-style interceptors for cross-cutting concerns like validation, logging, and security.
  name: Interceptor Framework
- description: Automatic type conversion between HTTP request parameters and Java types.
  name: Type Conversion
- description: Object-Graph Navigation Language for dynamic data binding and expression evaluation.
  name: OGNL Expression Language
- description: Template composition via Apache Tiles for reusable page layouts.
  name: Tiles Integration
- description: Convention-based REST API support with content type negotiation.
  name: REST Plugin
- description: Native Spring Framework integration for dependency injection.
  name: Spring Integration
finops:
- name: Apache Struts Finops
  service_category: API
  slug: apache-struts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-struts.png
integrations:
- description: Native Spring IoC container integration for dependency injection.
  name: Spring Framework
- description: Hibernate ORM integration for database persistence in action classes.
  name: Hibernate
- description: Template composition framework for reusable page layouts and components.
  name: Apache Tiles
- description: FreeMarker template engine support as an alternative to JSP views.
  name: FreeMarker
- description: Apache Velocity template engine for HTML view rendering.
  name: Velocity
layout: provider
modified: '2026-04-19'
name: Apache Struts
nav: Providers
network: true
overview: 'Apache Struts publishes 1 API on the [APIs.io](https://apis.io/) network: resource API. Tagged areas include Java, MVC, Web Applications, Web Framework, and Open-Source.


  Apache Struts'' developer surface includes authentication, documentation, developer portal, getting-started guide, release notes, support, FAQ, and 10 more developer resources.'
plans:
- name: Apache Struts Plans Pricing
  plan_count: 3
  slug: apache-struts-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Apache Struts Rate Limits
  slug: apache-struts-rate-limits
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 52.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-struts/refs/heads/main/screenshots/apache-struts-2026-06-20T172148.png
security:
- kind: authentication
  name: Apache Struts Authentication
  slug: apache-struts-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Struts Domain Security
  slug: apache-struts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Struts Vulnerability Disclosure
  slug: apache-struts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-struts
tags:
- Java
- MVC
- Web Applications
- Web Framework
- Open-Source
use_cases:
- description: Build large-scale Java web applications with clean MVC separation.
  name: Enterprise Java Web Applications
- description: Create REST APIs using the Struts REST plugin with JSON/XML content negotiation.
  name: RESTful Web Services
- description: Complex form processing with server-side validation and type conversion.
  name: Form-Based Applications
website: https://struts.apache.org/
---
