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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getcraft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcraft.com
- group: company
  title: ''
  type: Blog
  url: https://marketingcraft.getcraft.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getcraft.com/en/knowledge
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getcraft.com/terms-and-condition
- group: start
  title: ''
  type: SignUp
  url: https://getcraft.com/sign-up-home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetCraft
- group: auth
  title: ''
  type: SecurityPolicy
  url: security/getcraft-security-policy.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getcraft-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Every GetCraft host is dark — getcraft.com and api.getcraft.com sit behind a Google Cloud load balancer that answers HTTP 502 on every path including / and /.well-known/*, help.getcraft.com (HubSpot) and marketingcraft.getcraft.com (Webflow) both fail the TLS handshake with deprovisioned certificates, and the getcraft.com registration expires 2026-08-27 with no renewal since 2025-08-12; the only GetCraft surface still serving is its 2020-vintage security-policy GitBook.
  evidence:
  - status: 502
    url: https://getcraft.com/
  - status: 502
    url: https://api.getcraft.com/openapi.json
  - status: 502
    url: https://getcraft.com/.well-known/agent-card.json
  - status: 200
    url: https://getcraft.gitbook.io/security-policy
  reason: defunct
  state: none
created: '2026-07-17'
description: GetCraft is a Southeast Asian creative and content-marketing marketplace, headquartered in Indonesia and backed by 500 Global, that brands itself as "The Creative Industry's Premium Directory." It connects brands and agencies with a vetted network of freelance creators and production partners ("Crafters") for content, video, design, advertising, and marketing work, spanning a talent Directory, a Jobs board, Managed project services, and a Community. Its companion publication, MarketingCraft, is a bilingual (English/Indonesian) content hub of articles, events, tutorials, jobs, and research for marketers and creators. GetCraft exposes no public developer or API surface; this record is an identity/enrichment profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getcraft.png
layout: provider
modified: '2026-08-12'
name: GetCraft
nav: Providers
network: true
overview: 'GetCraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Marketing, Creative Marketplace, Freelance Talent, and Advertising.


  GetCraft''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
random_paper: 103
score:
  band: emerging
  composite: 13.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Getcraft Domain Security
  slug: getcraft-domain-security
  summary_line: TLSv1.3
slug: getcraft
tags:
- Company
- Content Marketing
- Creative Marketplace
- Freelance Talent
- Advertising
- Marketing
- Indonesia
- Southeast Asia
website: https://getcraft.com
---
