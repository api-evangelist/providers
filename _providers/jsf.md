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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Jakarta Faces specification for building component-based web user interfaces in Java applications. Defines a UI component model, state management, event handling, validation, navigation, and Facel
  name: Jakarta Faces
  slug: jsf
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jsf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jakarta.ee/specifications/faces/
- group: docs
  title: ''
  type: Documentation
  url: https://jakarta.ee/specifications/faces/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jakartaee/faces
created: '2025-01-01'
description: Jakarta Faces (formerly JavaServer Faces / JSF) is an MVC framework for building component-based user interfaces for Java web applications. It simplifies the development of web UIs through a component-driven approach with managed beans, an event-driven programming model, page navigation, state management, input validation, and built-in support for internationalization and accessibility. Jakarta Faces 4.1 is the current stable release with Jakarta EE 11, with 5.0 in development for Jakarta EE 12.
finops:
- name: Jsf Finops
  service_category: API
  slug: jsf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jsf.png
layout: provider
modified: '2026-04-28'
name: JSF
nav: Providers
network: true
overview: 'JSF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Java, JSF, Jakarta EE, MVC, and UI Components.


  JSF''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Jsf Plans Pricing
  plan_count: 3
  slug: jsf-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Jsf Rate Limits
  slug: jsf-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jsf/refs/heads/main/screenshots/jsf-2026-06-20T183812.png
security:
- kind: domain-security
  name: Jsf Domain Security
  slug: jsf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jsf
tags:
- Java
- JSF
- Jakarta EE
- MVC
- UI Components
- Web Framework
website: https://jakarta.ee/specifications/faces/
---
