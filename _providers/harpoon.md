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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harpoon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://harpoon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.harpoon.io/en/latest/
- group: commercial
  title: ''
  type: Pricing
  url: https://harpoon.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.harpooncorp.com/register
- group: start
  title: ''
  type: Login
  url: https://app.harpooncorp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harpoon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harpoon.io/privacy
created: '2026-07-17'
description: Harpoon is a no-code Kubernetes deployment platform that lets teams deploy commercial or open-source software to Kubernetes clusters in seconds using a drag-and-drop interface, without writing code or configuration scripts. It automates cloud account security, cluster provisioning and autoscaling across AWS, Azure, Google Cloud and VMware, and integrates with CI/CD tooling such as GitHub, GitLab, Jenkins, Argo, Docker Hub and Harbor. The product is delivered as a hosted web application (app.harpooncorp.com) aimed at both startups and enterprises; it is surfaced here as an a16z portfolio lead. As of this enrichment pass Harpoon publishes no public REST API, OpenAPI specification, SDK, CLI or webhook surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harpoon.png
layout: provider
modified: '2026-07-20'
name: Harpoon
nav: Providers
network: true
overview: 'Harpoon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Kubernetes, Deployment, DevOps, and Cloud.


  Harpoon''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harpoon/refs/heads/main/screenshots/harpoon-2026-07-25T220746.png
security:
- kind: domain-security
  name: Harpoon Domain Security
  slug: harpoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harpoon
tags:
- Company
- Kubernetes
- Deployment
- DevOps
- Cloud
- No-Code
- Containers
- Platform Engineering
website: https://harpoon.io/
---
