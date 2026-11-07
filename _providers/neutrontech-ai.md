---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/neutrontech-ai/llms/neutrontech-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neutrontech-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/neutrontech-ai/well-known/neutrontech-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/neutrontech-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/neutrontech-ai/mcp/neutrontech-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/neutrontech-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/neutrontech-ai/hosts/neutrontech-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neutrontech-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/neutrontech-ai/integrations/neutrontech-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/neutrontech-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/neutrontech-ai/vendors/neutrontech-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/neutrontech-ai-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://neutrontech.ai
- group: auth
  href: https://artifacts.apis.io/neutrontech-ai/security/neutrontech-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neutrontech-ai-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.neutrontech.ai
- group: operate
  title: ''
  type: Support
  url: https://support.neutrontech.ai/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neutrontech.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neutrontech.ai/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/neutrontechai
- group: other
  title: ''
  type: X
  url: https://x.com/neutrontechai
- group: other
  title: ''
  type: Email
  url: mailto:sales@neutrontech.ai
created: '2026-10-22'
description: NeutronTech is an Apple-focused software company building private, on-device software for iPhone and Mac. Its products are Hubyn (a private, end-to-end encrypted team messenger and workspace that connects people by an 8-character PIN instead of a phone number), Neutron Studio (a private local-AI app for Mac that answers questions over your own documents with citations, and the company's AI research vehicle), and Neutron Health (offline clinic software, in development). The site publishes no public developer API, documentation or API reference.
image: https://neutrontech.ai/neutrontech-share.jpg
layout: provider
mcp_servers:
- description: NeutronTech serves no MCP server for its products. Its blog, blog.neutrontech.ai, is a WordPress.com-hosted site (wpcomsh, Jetpack and wpcom namespaces in the REST index) whose REST API carries the Wo
  name: NeutronTech blog MCP (WordPress.com MCP adapter)
  slug: neutrontech-blog-mcp-wordpress-com-mcp-adapter
modified: '2026-10-22'
name: NeutronTech
nav: Providers
network: true
overview: 'NeutronTech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apple, iPhone, Mac, and Privacy.


  NeutronTech''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Neutrontech Ai Plans Pricing
  plan_count: 0
  slug: neutrontech-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Neutrontech Ai Rate Limits
  slug: neutrontech-ai-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 58.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.0
  provenance:
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/neutrontech-ai/neutrontech-ai-2026-11-03T140144.png
security:
- kind: domain-security
  name: Neutrontech Ai Domain Security
  slug: neutrontech-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neutrontech-ai
tags:
- Company
- Apple
- iPhone
- Mac
- Privacy
- On-Device AI
- Local AI
- Messaging
- Healthcare
website: https://neutrontech.ai
---
