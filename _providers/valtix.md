---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Valtix Alerts Webhooks
  slug: valtix-alerts-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valtix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.valtix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.valtix.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.valtix.com/tutorials/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.valtix.com/faq/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valtix-security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.valtix.com/releases/overview/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valtix-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valtix-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/valtix-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valtix-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/valtix-alerts-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valtix-llms.txt
created: '2026-07-17'
description: Valtix is a multicloud network security platform delivering agentless, cloud-native firewalling — ingress WAF/IDS/IPS, egress TLS decryption and exfiltration prevention, and east-west inspection — across AWS, Azure, GCP, and OCI, driven by continuous cloud asset discovery and tag-based dynamic policy. Founded in 2018 and acquired by Cisco in 2023, the product is sold today as Cisco Multicloud Defense; the Valtix documentation site and the verified Terraform provider (valtix-security/valtix) remain live and actively maintained under the Valtix name, while the standalone website and commercial pages redirect to Cisco.
image: https://avatars.githubusercontent.com/valtix-security
layout: provider
modified: '2026-08-19'
name: Valtix
nav: Providers
network: true
overview: 'Valtix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, Network Security, and Multi-Cloud.


  The Valtix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Valtix''s developer surface includes documentation, getting-started guide, support, changelog, authentication, and 9 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 27.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valtix/refs/heads/main/screenshots/valtix-2026-09-02T165339.png
security:
- kind: authentication
  name: Valtix Authentication
  slug: valtix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valtix Domain Security
  slug: valtix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valtix
tags:
- Company
- Security
- Cloud Security
- Network Security
- Multi-Cloud
- Firewall
- Terraform
website: https://www.valtix.com
---
