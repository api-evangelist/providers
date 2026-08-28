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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendulum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pendulumlife.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pendulum-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pendulum-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pendulum-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pendulumlife.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pendulumlife.com/policies/terms-of-service
created: '2026-07-17'
description: Pendulum (Pendulum Therapeutics, pendulumlife.com) is a microbiome-management and metabolic-health company that develops clinically validated probiotic supplements built on novel, patented anaerobic microbial strains such as Akkermansia muciniphila. Its consumer products - including Glucose Control, Metabolic Daily, Akkermansia, and a GLP-1 probiotic - are formulated to fuel and maintain the gut lining, support immunity, relieve gas and bloating, and help keep blood glucose in a healthy range, differentiated by double-blind, placebo-controlled clinical trials rather than off-the-shelf probiotic blends. Pendulum is a direct-to-consumer health and supplement brand and is a portfolio company of DCVC; it does not currently publish a public developer API surface.
image: https://pendulumlife.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Pendulum store UCP commerce (Shopify)
  slug: pendulum-store-ucp-commerce-shopify
modified: '2026-07-20'
name: Pendulum
nav: Providers
network: true
overview: Pendulum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Microbiome, Probiotics, and Metabolic Health.
random_paper: 13
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  provenance:
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Pendulum Domain Security
  slug: pendulum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pendulum
tags:
- Company
- Health
- Microbiome
- Probiotics
- Metabolic Health
- Consumer Health
- Supplements
- Direct to Consumer
website: https://pendulumlife.com
---
