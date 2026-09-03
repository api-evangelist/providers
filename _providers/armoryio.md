---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.armory.io/'', ''status'': 301, ''note'': ''declared website redirects to https://www.harness.io:443/products/continuous-delivery — a different registrable domain (armory.io -> harness.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/harness/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armoryio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.armory.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.armory.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armory
- group: build
  title: ''
  type: Packages
  url: packages/armoryio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/armoryio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armoryio-llms.txt
created: '2026-07-17'
description: Armory.io was an enterprise continuous delivery and continuous deployment company built around the open-source Spinnaker project. Its products included Armory Continuous Deployment Self-Hosted and Managed (an enterprise Spinnaker distribution), Armory Continuous Deployment-as-a-Service (CDaaS) with a declarative GitOps deployment experience, and the Armory Scale Agent for Spinnaker and Kubernetes. Armory was backed by Insight Partners and was later acquired by Harness; the armory.io website now 301-redirects to harness.io and the CDaaS cloud service, developer portal, and status page are decommissioned, while the documentation site (docs.armory.io) and the Apache-2.0 GitHub organization (github.com/armory) remain live.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/armoryio.png
layout: provider
modified: '2026-07-18'
name: Armory.io
nav: Providers
network: true
overview: 'Armory.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Continuous Delivery, Continuous Deployment, and Spinnaker.


  Armory.io''s developer surface includes documentation and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armoryio/refs/heads/main/screenshots/armoryio-2026-07-25T201231.png
security:
- kind: domain-security
  name: Armoryio Domain Security
  slug: armoryio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: armoryio
tags:
- Company
- DevOps
- Continuous Delivery
- Continuous Deployment
- Spinnaker
- Kubernetes
- Deployment
- GitOps
website: https://www.armory.io/
---
