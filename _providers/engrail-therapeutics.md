---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The public, anonymously-readable content API exposed by engrail.com at /wp-json/wp/v2. Sixteen read operations over posts, pages, media, categories, tags, comments, and the site's own type/taxonomy/st
  name: Engrail Therapeutics Site Content API
  slug: content
- description: Two live Model Context Protocol servers registered under the `mcp` REST namespace on engrail.com, fronted by RFC 8414 and RFC 9728 OAuth discovery documents at the apex. Both are OAuth-protected — ano
  name: Engrail Therapeutics MCP Servers
  slug: mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.engrail.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/engrail-therapeutics_stock/
- group: company
  title: ''
  type: About
  url: https://www.engrail.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.engrail.com/investors-media/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.engrail.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.engrail.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engrail.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engrail.com/privacy-policy/
- group: commercial
  title: ''
  type: LegalDisclaimer
  url: https://www.engrail.com/legal-disclaimer/
- group: company
  title: ''
  type: Careers
  url: https://www.engrail.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://www.engrail.com/partners/
- group: other
  title: ''
  type: Pipeline
  url: https://www.engrail.com/pipeline/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/engrail-therapeutics
- group: agent
  title: ''
  type: WellKnown
  url: well-known/engrail-therapeutics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/engrail-therapeutics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/engrail-therapeutics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/engrail-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/engrail-therapeutics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/engrail-therapeutics-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engrail-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/engrail-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Engrail Therapeutics is a clinical-stage precision-neuroscience pharmaceutical company founded in 2019 and headquartered in San Diego, California. It applies precision chemistry and pharmacology to scientifically validated mechanisms of action, developing targeted small-molecule therapies for neuropsychiatric and neurodevelopmental diseases with significant unmet need — including generalized anxiety disorder, major depressive disorder characterized by anhedonia, post-traumatic stress disorder and rare neurodegenerative conditions. Its lead program, ENX-102, is a highly selective GABA-A alpha-2,3,5 positive allosteric modulator in Phase 2 (the ENCALM trial) for generalized anxiety disorder; ENX-104 is in clinical development for anhedonic depression. The company closed an oversubscribed $157M Series B in March 2024 co-led by F-Prime Capital, Forbion and Norwest Venture Partners, bringing total capital raised since inception past $220M. Engrail publishes no product or developer
  API; the machine-readable surfaces catalogued here are the public read-only content API and the OAuth-protected Model Context Protocol servers exposed by its corporate website.
image: https://www.engrail.com/wp-content/uploads/2022/05/logo.png
layout: provider
mcp_servers:
- description: ''
  name: engrail-therapeutics-mcp.yml
  slug: engrail-therapeutics-mcpyml
modified: '2026-08-01'
name: Engrail Therapeutics
nav: Providers
network: true
overview: 'Engrail Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: Site Content API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Neuroscience.


  Engrail Therapeutics'' developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
random_paper: 108
scopes:
- name: Engrail Therapeutics Scopes
  scope_count: 1
  slug: engrail-therapeutics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 62.8
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 37.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/engrail-therapeutics/refs/heads/main/screenshots/engrail-therapeutics-2026-08-07T164922.png
security:
- kind: authentication
  name: Engrail Therapeutics Authentication
  slug: engrail-therapeutics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Engrail Therapeutics Domain Security
  slug: engrail-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: engrail-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Neuroscience
- Clinical Trials
- Drug Development
- Healthcare
- Mental Health
- Model Context Protocol
website: https://www.engrail.com/
---
