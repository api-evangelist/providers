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
- description: Merbridge uses eBPF to accelerate service mesh data planes by replacing iptables-based traffic interception and shortening the datapath between sidecars and services. It is a CNCF Sandbox project comp
  name: Merbridge
  slug: merbridge
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/merbridge/merbridge/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/merbridge/merbridge/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/merbridge/merbridge/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/merbridge/merbridge/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merbridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merbridge.io/
- group: docs
  title: ''
  type: Documentation
  url: https://merbridge.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merbridge
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/merbridge/merbridge
- group: company
  title: ''
  type: Blog
  url: https://merbridge.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/merbridge/shared_invite/zt-11uc3z0w7-DMyv42eQ6s5YUxO5mZ5hwQ
- group: other
  title: ''
  type: Group
  url: https://groups.google.com/g/merbridge
created: '2026-04-28'
description: Merbridge is an open source, eBPF-based service mesh acceleration tool that replaces iptables rules with eBPF traffic interception and uses msg_redirect to shorten the datapath between sidecars and services. It is a CNCF Sandbox project and supports Istio, Linkerd2, and Kuma.
finops:
- name: Merbridge Finops
  service_category: API
  slug: merbridge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/merbridge.png
layout: provider
modified: '2026-04-28'
name: Merbridge
nav: Providers
network: true
overview: 'Merbridge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CNCF, eBPF, Networking, Performance, and Service Mesh.


  Merbridge''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Merbridge Plans Pricing
  plan_count: 3
  slug: merbridge-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Merbridge Rate Limits
  slug: merbridge-rate-limits
score:
  band: emerging
  composite: 18.3
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
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 18.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merbridge/refs/heads/main/screenshots/merbridge-2026-06-20T185149.png
security:
- kind: domain-security
  name: Merbridge Domain Security
  slug: merbridge-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: merbridge
tags:
- CNCF
- eBPF
- Networking
- Performance
- Service Mesh
website: https://merbridge.io/
---
