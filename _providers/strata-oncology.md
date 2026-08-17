---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-17'
api_count: 10
apis:
- description: Registered types, taxonomies and statuses.
  name: Strata Oncology Discovery API
  slug: strata-oncology-discovery-api
- description: Uploaded media items.
  name: Strata Oncology Media API
  slug: strata-oncology-media-api
- description: Website pages.
  name: Strata Oncology Pages API
  slug: strata-oncology-pages-api
- description: Blog posts.
  name: Strata Oncology Posts API
  slug: strata-oncology-posts-api
- description: Press releases and published research.
  name: Strata Oncology Publications API
  slug: strata-oncology-publications-api
- description: Patient and provider resource documents.
  name: Strata Oncology Resources API
  slug: strata-oncology-resources-api
- description: Cross-content-type search.
  name: Strata Oncology Search API
  slug: strata-oncology-search-api
- description: Categories and tags.
  name: Strata Oncology Taxonomy API
  slug: strata-oncology-taxonomy-api
- description: Leadership and team member profiles.
  name: Strata Oncology Team API
  slug: strata-oncology-team-api
- description: Published testimonials.
  name: Strata Oncology Testimonials API
  slug: strata-oncology-testimonials-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Strata Oncology Website Content Discovery API
  slug: open-strata-oncology-discovery-api
- collection_type: open
  name: Strata Oncology Website Content Media API
  slug: open-strata-oncology-media-api
- collection_type: open
  name: Strata Oncology Website Content Pages API
  slug: open-strata-oncology-pages-api
- collection_type: open
  name: Strata Oncology Website Content Posts API
  slug: open-strata-oncology-posts-api
- collection_type: open
  name: Strata Oncology Website Content Publications API
  slug: open-strata-oncology-publications-api
- collection_type: open
  name: Strata Oncology Website Content Resources API
  slug: open-strata-oncology-resources-api
- collection_type: open
  name: Strata Oncology Website Content Search API
  slug: open-strata-oncology-search-api
- collection_type: open
  name: Strata Oncology Website Content Taxonomy API
  slug: open-strata-oncology-taxonomy-api
- collection_type: open
  name: Strata Oncology Website Content Team API
  slug: open-strata-oncology-team-api
- collection_type: open
  name: Strata Oncology Website Content Testimonials API
  slug: open-strata-oncology-testimonials-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/strata-oncology-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/strata-oncology-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://strataoncology.com/
- group: company
  title: ''
  type: About
  url: https://strataoncology.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://strataoncology.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://strataoncology.com/news-and-publications/
- group: company
  title: ''
  type: BlogRSS
  url: https://strataoncology.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://strataoncology.com/create-account/
- group: start
  title: ''
  type: Login
  url: https://portal.strataoncology.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strataoncology.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strataoncology.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://strataoncology.com/privacy-practices/
- group: other
  title: ''
  type: NoSurprisesAct
  url: https://strataoncology.com/no-surprises-act/
- group: commercial
  title: ''
  type: Billing
  url: https://strataoncology.com/resources/patient-billing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StrataOncology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/strata-oncology/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StrataOncology
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/strata-oncology_stock/
- group: design
  title: ''
  type: Conventions
  url: conventions/strata-oncology-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strata-oncology-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strata-oncology-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/strata-oncology-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strata-oncology-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strata-oncology-domain-security.yml
created: '2026-08-02'
description: Strata Oncology is a precision oncology company founded in 2015 by Dan Rhodes and Scott Tomlins and headquartered in Ann Arbor, Michigan. It develops and runs predictive biomarker tests out of its own high-throughput CLIA laboratory, including StrataNGS tumor genomic profiling, the Immunotherapy Response Score for anti-PD-1/PD-L1 monotherapy benefit, PD-L1 IHC testing, and Antibody-Drug Conjugate Treatment Response Scores. Testing is delivered to health systems through the Strata Precision Oncology Network, with ordering and results handled through the login-gated Strata Request Portal and the Strata Assistant app distributed in the Epic App Orchard. Strata Oncology publishes no public developer program or API documentation; the only anonymous machine-readable surface API Evangelist could verify is the WordPress REST content API behind strataoncology.com.
image: https://strataoncology.com/wp-content/uploads/2022/09/Strata-Oncology-Logo_Symbol-Dark-Theme.svg
layout: provider
mcp_servers:
- description: ''
  name: strata-oncology-mcp.yml
  slug: strata-oncology-mcpyml
modified: '2026-08-02'
name: Strata Oncology
nav: Providers
network: true
overview: 'Strata Oncology publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, Pages API, and 7 more. Tagged areas include Company, Healthcare, Precision Medicine, Oncology, and Genomics.


  Strata Oncology''s developer surface includes engineering blog, signup flow, and 23 more developer resources.'
random_paper: 84
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 14.4
    developer_ergonomics: 6.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 24.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Strata Oncology Authentication
  slug: strata-oncology-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Strata Oncology Domain Security
  slug: strata-oncology-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: strata-oncology
tags:
- Company
- Healthcare
- Precision Medicine
- Oncology
- Genomics
- Diagnostics
- Laboratory
- Life Sciences
- Biomarkers
- Clinical Trials
website: https://strataoncology.com/
---
