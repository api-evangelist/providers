---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'A remote, anonymous Model Context Protocol server served from the NeuroTherapia corporate domain at /_api/mcp. It is provisioned by the Wix website platform rather than authored by NeuroTherapia, and '
  name: NeuroTherapia Site MCP
  slug: neurotherapia-site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neurotherapia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neurotherapia.com/
- group: operate
  title: ''
  type: Support
  url: https://www.neurotherapia.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.neurotherapia.com/company-news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.neurotherapia.com/blog-feed.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neurotherapia.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neurotherapia.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurotherapia-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neurotherapia-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neurotherapia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neurotherapia-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neurotherapia-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/neurotherapia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neurotherapia-rate-limits.yml
created: '2026-08-26'
description: 'NeuroTherapia, Inc. is a clinical-stage, privately held biotechnology company spun out of the Cleveland Clinic in 2015 by physician-scientists Mohamed Naguib and Joseph Foss. Headquartered in Gates Mills, Ohio, it develops oral small-molecule drugs targeting neuroinflammatory conditions of the central nervous system, including Alzheimer''s disease, Parkinson''s disease, ALS and neuropathic pain. Its lead candidate NTRX-07 is an orally available selective cannabinoid type 2 (CB2) receptor agonist that restores normal microglial function, reducing neuroinflammation and amyloid-beta levels while improving synaptic plasticity, learning and memory in preclinical models; the company has completed a Phase 2a trial in Alzheimer''s patients and holds EMA approval for a Phase 2 trial. NeuroTherapia is a therapeutics developer, not a software or API vendor: it publishes no developer program, no product API and no SDKs. Its only machine-readable surface is the Wix-platform site MCP server
  and llms.txt it serves from its own corporate domain.'
image: https://static.wixstatic.com/media/f2ff6e_19fb09e81a294b0ea0376a869b29bf0a~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: NeuroTherapia, Inc.
  slug: neurotherapia-inc
modified: '2026-08-26'
name: NeuroTherapia
nav: Providers
network: true
overview: 'NeuroTherapia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Life Sciences, Health, and Clinical Trials.


  NeuroTherapia''s developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: Neurotherapia Plans Pricing
  plan_count: 0
  slug: neurotherapia-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Neurotherapia Rate Limits
  slug: neurotherapia-rate-limits
score:
  band: emerging
  composite: 20.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Neurotherapia Authentication
  slug: neurotherapia-authentication
  summary_line: none/bearer-visitor-token · 2 schemes
- kind: domain-security
  name: Neurotherapia Domain Security
  slug: neurotherapia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neurotherapia
tags:
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Health
- Clinical Trials
- Neuroscience
- Drug Discovery
- Alzheimers Disease
- Company
website: https://www.neurotherapia.com/
---
