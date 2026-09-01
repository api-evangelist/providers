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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcsight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opentext.com/products/arcsight-enterprise-security-manager
- group: docs
  title: ''
  type: Documentation
  url: https://www.microfocus.com/documentation/arcsight/
- group: operate
  title: ''
  type: Support
  url: https://community.opentext.com/cyberres/arcsight/
created: '2026-07-17'
description: ArcSight is an enterprise security information and event management (SIEM) platform, now part of OpenText Cybersecurity (formerly Micro Focus, and HP before that). The ArcSight family centers on Enterprise Security Manager (ESM) for real-time correlation and threat detection, alongside Logger for log management and compliance, SmartConnectors for data collection and normalization, Intelligence for behavioral analytics, and Recon for search and investigation. ArcSight was an early Kleiner Perkins portfolio company. It exposes REST and web-services APIs (ESM client services, Logger Web Services, and SCIM user provisioning) primarily to on-premises and SaaS customer deployments rather than as a public developer platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcsight.png
layout: provider
modified: '2026-07-18'
name: ArcSight
nav: Providers
network: true
overview: 'ArcSight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, SIEM, Cybersecurity, and Threat Detection.


  ArcSight''s developer surface includes documentation, support, and 2 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arcsight/refs/heads/main/screenshots/arcsight-2026-07-25T201054.png
security:
- kind: domain-security
  name: Arcsight Domain Security
  slug: arcsight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcsight
tags:
- Company
- Security
- SIEM
- Cybersecurity
- Threat Detection
- Log Management
- Compliance
- Enterprise Security
website: https://www.opentext.com/products/arcsight-enterprise-security-manager
---
