---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jcr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jcp.org/en/jsr/detail?id=283
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://jackrabbit.apache.org
- group: docs
  title: ''
  type: Specification
  url: http://jcp.org/aboutJava/communityprocess/final/jsr283/index.html
created: '2025-01-01'
description: JCR (Java Content Repository) is a Java specification (JSR-283, "Content Repository for Java Technology API 2.0") that provides a vendor-neutral, implementation-independent way to access content bi-directionally on a granular level within a content repository. It defines features for hierarchical content modeling, versioning, access control, search, locking, and observation, with the javax.jcr package as its core. The reference implementation is provided by the Apache Jackrabbit project.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jcr.png
layout: provider
modified: '2026-04-28'
name: JCR
nav: Providers
network: true
overview: JCR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Repository, Java, JCR, and JSR-283.
random_paper: 21
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jcr/refs/heads/main/screenshots/jcr-2026-06-20T183711.png
security:
- kind: domain-security
  name: Jcr Domain Security
  slug: jcr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jcr
tags:
- CMS
- Content Repository
- Java
- JCR
- JSR-283
- Standard
website: https://jcp.org/en/jsr/detail?id=283
---
