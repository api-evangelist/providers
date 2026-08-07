---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.nerc.com/
- group: start
  title: ''
  type: Portal
  url: https://eroportal.nerc.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/standards/reliability-standards
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/programs/registration/compliance-registry-files
- group: other
  title: ''
  type: DataCatalog
  url: https://www.nerc.com/globalassets/programs/registration/compliance-registry-files/nerc_compliance_registry_matrix_excel.xlsx
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/programs/reliability-assessment--performance-analysis/generating-availability-data-system
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/programs/reliability-assessment--performance-analysis/transmission-availability-data-system
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/applications/align-and-secure-evidence-locker-sel
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/applications/centralized-organization-registration-ero-system-cores-technology-project
- group: docs
  title: ''
  type: Documentation
  url: https://www.nerc.com/applications/nerc-data-stores--extranet-sites
- group: operate
  title: ''
  type: Support
  url: https://support.nerc.net/
- group: company
  title: ''
  type: Blog
  url: https://www.nerc.com/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nerc.com/legal-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nerc.com/terms-of-use-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/north-american-electric-reliability-corporation/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/NERC_Official
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@NERCOfficial
- group: company
  title: ''
  type: Website
  url: https://www.eisac.com/
- group: company
  title: ''
  type: Website
  url: https://www.nercalerts.com/index.php
- group: operate
  title: ''
  type: Roadmap
  url: https://www.nerc.com/standards/reliability-standards-under-development
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nerc-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/nerc-eisac-openid-configuration.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/nerc-robots.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nerc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nerc-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nerc-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nerc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nerc-llms.txt
created: '2026-07-27'
description: 'The North American Electric Reliability Corporation (NERC) is the not-for-profit international regulatory authority certified by FERC in July 2006 as the Electric Reliability Organization under Section 215 of the Federal Power Act, added by the Energy Policy Act of 2005. From offices in Washington, DC and Atlanta, and working through six Regional Entities (MRO, NPCC, RF, SERC, Texas RE, WECC), NERC develops and enforces the mandatory Reliability Standards, including the CIP cyber security standards, that govern the bulk power system across the contiguous United States, all of Canada, and a portion of Baja California, Mexico. It registers and certifies the entities that operate that system, monitors and enforces compliance, runs the Electricity Information Sharing and Analysis Center (E-ISAC), and collects mandatory industry performance data through Rules of Procedure Section 1600 data requests into GADS, TADS, DADS and MIDAS. NERC sits at the top of the North American bulk-power
  value chain, above the ISOs/RTOs, transmission owners and generator owners it registers, and entirely above the retail utility-to-customer relationship. Its API posture is the plainest in this series. NERC publishes NO developer API, NO OpenAPI, NO SDK, NO developer portal and NO open data portal. A site search of nerc.com for the term API on 2026-07-27 returned zero matching documents. NERC is a MANDATOR of energy data, not a publisher of it. The obligation it imposes is to SUBMIT data upward to NERC, and the data submitted is explicitly confidential under Rules of Procedure Section 1500. What NERC does publish anonymously is documents: reliability assessments, the State of Reliability report, aggregated GADS/TADS statistics, Power BI dashboards and the public NERC Compliance Registry Matrix spreadsheet of every registered entity. Everything machine-facing, including the ERO Portal, Align, the Secure Evidence Locker, CORES, the GADS/TADS data stores and the E-ISAC portal, is behind an
  approved account. No Green Button, no ESPI, no consumer data right, and no consumer usage or billing API exists anywhere in NERC''s surface, because retail customer data is outside its reach entirely. NERC is a regulator whose peer FERC publishes a documented public API and whose neighbour EIA publishes one of the best government APIs anywhere, while NERC itself publishes none.'
image: https://www.nerc.com/globalassets/nerc-logo.png
layout: provider
modified: '2026-07-27'
name: NERC
nav: Providers
network: true
overview: 'NERC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Canada, Electricity, and Grid.


  NERC''s developer surface includes developer portal, documentation, support, engineering blog, YouTube channel, authentication, and 22 more developer resources.'
random_paper: 85
scopes:
- name: Nerc Scopes
  scope_count: 36
  slug: nerc-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 24.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Nerc Authentication
  slug: nerc-authentication
  summary_line: none/oauth2/openIdConnect · 0 schemes
- kind: domain-security
  name: Nerc Domain Security
  slug: nerc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nerc
tags:
- Energy
- United States
- Canada
- Electricity
- Grid
- Regulator
- Government
- Reliability
- Bulk Power System
- Critical Infrastructure
- Cyber Security
- Energy Markets
- Compliance
website: https://www.nerc.com/
---
