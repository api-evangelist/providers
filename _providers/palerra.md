---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://palerra.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.oracle.com/corporate/acquisitions/palerra/index.html — a different registrable domain (palerra.com -> oracle.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: https://apis.io/providers/oracle/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palerra-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/palerra
- group: company
  title: ''
  type: Website
  url: https://palerra.com
created: '2026-07-17'
description: 'Palerra, Inc. was a Santa Clara, California cloud security company whose LORIC platform delivered Cloud Access Security Broker (CASB) capabilities: automated security monitoring, threat detection, configuration management, and compliance across SaaS and IaaS environments such as Salesforce, AWS, Microsoft Office 365, ServiceNow, and Box. Backed by Norwest Venture Partners and Wing Venture Capital, Palerra was acquired by Oracle in September 2016 and folded into the Oracle CASB Cloud Service. The palerra.com domain now redirects to Oracle''s cloud security portal, and no independent public API, developer portal, or machine-readable specification remains.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/palerra.png
layout: provider
modified: '2026-08-21'
name: Palerra
nav: Providers
network: true
overview: Palerra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud Security, CASB, and SaaS Security.
random_paper: 8
score:
  band: minimal
  composite: 5.3
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/palerra/refs/heads/main/screenshots/palerra-2026-08-07T191315.png
security:
- kind: domain-security
  name: Palerra Domain Security
  slug: palerra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: palerra
tags:
- Company
- Security
- Cloud Security
- CASB
- SaaS Security
- Compliance
- Acquired
website: https://palerra.com
---
