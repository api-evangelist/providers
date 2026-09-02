---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The CrowdStrike API provides access to platform services and data for enterprise integration and automation.
  name: CrowdStrike API
  slug: crowdstrike-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/crowdstrike-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdstrike-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdstrike-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrowdStrike
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crowdstrike
- group: company
  title: ''
  type: Website
  url: https://www.crowdstrike.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.crowdstrike.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.crowdstrike.com/blog/feed/
created: '2026-04-19'
description: CrowdStrike is a major US corporation and Fortune 1000 company. The CrowdStrike API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Crowdstrike Finops
  service_category: Cybersecurity
  slug: crowdstrike-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the CrowdStrike Falcon platform. CrowdStrike exposes its capabilities through an OAuth2-based REST API; this schema models that surface as Graph
  name: CrowdStrike GraphQL Schema
  slug: crowdstrike-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdstrike.png
layout: provider
modified: '2026-04-19'
name: CrowdStrike
nav: Providers
network: true
overview: 'CrowdStrike publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity and Endpoint Security.


  CrowdStrike''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Crowdstrike Plans Pricing
  plan_count: 4
  slug: crowdstrike-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Crowdstrike Rate Limits
  slug: crowdstrike-rate-limits
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdstrike/refs/heads/main/screenshots/crowdstrike-2026-06-20T175254.png
security:
- kind: domain-security
  name: Crowdstrike Domain Security
  slug: crowdstrike-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crowdstrike Vulnerability Disclosure
  slug: crowdstrike-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crowdstrike Trust Center
  slug: crowdstrike-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: crowdstrike
tags:
- Cybersecurity
- Endpoint Security
website: https://www.crowdstrike.com
---
