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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Wicket Component API provides the core Java classes for building web UIs. Pages extend WebPage, components extend Panel, Form, Link, Button, and other base classes. The model system uses IModel<T>
  name: Apache Wicket Component API
  slug: apache-wicket-component-api
artifact_total: 19
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/wicket/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/wicket/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/wicket/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-wicket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-wicket-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/wicket
- group: docs
  title: ''
  type: Documentation
  url: https://wicket.apache.org/learn/
- group: start
  title: ''
  type: Portal
  url: https://wicket.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://wicket.apache.org/start/quickstart.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/wicket/releases
- group: operate
  title: ''
  type: Support
  url: https://wicket.apache.org/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: company
  title: ''
  type: Blog
  url: https://wicket.apache.org/atom.xml
created: '2026-03-16'
description: Apache Wicket is a component-based web application framework for Java that provides a clean separation of markup and logic with a stateful component model. It enables developers to build web applications using pure Java and HTML, without XML configuration. Wicket's stateful model stores component state on the server side while providing Ajax integration, type-safe page parameters, and deep testability. It is maintained by the Apache Software Foundation.
features:
- description: Server-side stateful component model with automatic state serialization and clustering support.
  name: Stateful Component Model
- description: No JSP, no annotations on HTML, no XML mappings - just Java classes and plain HTML templates.
  name: Pure Java and HTML
- description: Type-safe page parameters using PageParameters with automatic encoding/decoding.
  name: Type-Safe URLs
- description: Built-in Ajax behaviors and components for partial page updates without JavaScript coding.
  name: Ajax Integration
- description: WicketTester class provides comprehensive unit testing without a running servlet container.
  name: Testability
- description: Built-in CSRF protection, authorization strategies, and secure page parameters.
  name: Security
finops:
- name: Apache Wicket Finops
  service_category: API
  slug: apache-wicket-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-wicket.png
integrations:
- description: SpringComponentInjector for Spring bean injection into Wicket components.
  name: Spring Framework
- description: CDI/Weld integration for Jakarta EE dependency injection in Wicket.
  name: CDI
- description: Hibernate model integration for domain objects bound to Wicket components.
  name: Hibernate
- description: Wicket Bootstrap library for Bootstrap CSS integration.
  name: Bootstrap
layout: provider
modified: '2026-04-19'
name: Apache Wicket
nav: Providers
network: true
overview: 'Apache Wicket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Component-Based, Java, Web Applications, Web Framework, and Open-Source.


  Apache Wicket''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, engineering blog, and 8 more developer resources.'
plans:
- name: Apache Wicket Plans Pricing
  plan_count: 3
  slug: apache-wicket-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Apache Wicket Rate Limits
  slug: apache-wicket-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: 1.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 23.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-wicket/refs/heads/main/screenshots/apache-wicket-2026-06-20T172157.png
security:
- kind: domain-security
  name: Apache Wicket Domain Security
  slug: apache-wicket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Wicket Vulnerability Disclosure
  slug: apache-wicket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-wicket
tags:
- Component-Based
- Java
- Web Applications
- Web Framework
- Open-Source
- AJAX
use_cases:
- description: Complex business applications with rich server-side state management.
  name: Enterprise Java Web Applications
- description: Data entry applications with complex validation and type conversion.
  name: Form-Intensive Applications
- description: CMS backends with hierarchical content management and editorial workflows.
  name: Content Management Systems
website: https://wicket.apache.org/
---
