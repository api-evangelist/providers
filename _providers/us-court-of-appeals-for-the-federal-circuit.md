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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Public Access to Court Electronic Records (PACER) provides online access to U.S. Federal Court case and docket information from Federal Courts including the U.S. Court of Appeals for the Federal Circu
  name: PACER - Public Access to Court Electronic Records
  slug: pacer
- description: 'Public access to U.S. Court of Appeals for the Federal Circuit opinions, orders, and judgments. Includes precedential opinions, Rule 36 judgments, non-ministerial orders, and errata. Available online '
  name: Federal Circuit Opinions and Orders
  slug: opinions-orders
- description: Case information and records for the U.S. Court of Appeals for the Federal Circuit. Cases filed on or after March 1, 2012, are available through PACER or at public terminals in the Clerk's Office. The
  name: Federal Circuit Case Records
  slug: case-records
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-court-of-appeals-for-the-federal-circuit-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cafc.uscourts.gov/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/court-of-appeals-for-the-federal-circuit
- group: company
  title: ''
  type: Website
  url: https://www.cafc.uscourts.gov/
- group: docs
  title: Case Information
  type: Documentation
  url: https://www.cafc.uscourts.gov/home/case-information/
- group: docs
  title: Opinions and Orders
  type: Documentation
  url: https://www.cafc.uscourts.gov/home/case-information/opinions-orders/
- group: start
  title: PACER Registration
  type: GettingStarted
  url: https://pacer.uscourts.gov/
- group: docs
  title: PACER Developer Resources
  type: APIReference
  url: https://pacer.uscourts.gov/file-case/developer-resources
- group: docs
  title: Rules and Procedures
  type: Documentation
  url: https://www.cafc.uscourts.gov/home/rules-procedures/
- group: operate
  title: Contact the Court
  type: Contact
  url: https://www.cafc.uscourts.gov/home/about-the-court/contact/
- group: design
  title: US Court of Appeals for the Federal Circuit Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/vocabulary/us-court-of-appeals-for-the-federal-circuit-vocabulary.yml
- group: design
  title: US Court of Appeals for the Federal Circuit JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/json-ld/us-court-of-appeals-for-the-federal-circuit-context.jsonld
created: '2024-12-25'
description: The US Court of Appeals for the Federal Circuit is a federal appellate court with nationwide jurisdiction over cases involving patent law, international trade, government contracts, federal employment, veterans' benefits, and other specialized areas of federal law. The court provides public access to opinions and orders online from 2004 to present, with full case records accessible via PACER for cases filed after March 1, 2012. The PACER system offers developer APIs including the Authentication API and the Case Locator (PCL) API for programmatic access to federal case data across all federal courts.
examples:
- key_count: 11
  name: Cafc Case Example
  slug: cafc-case-example
- key_count: 9
  name: Cafc Docket Entry Example
  slug: cafc-docket-entry-example
- key_count: 10
  name: Cafc Opinion Example
  slug: cafc-opinion-example
features:
- description: Programmatic access to the nationwide federal court case index via the PACER Case Locator (PCL) API, enabling searches for cases and associated parties across all federal courts including the Federal Circuit.
  name: PACER Case Locator API
- description: API allowing automated authentication to PACER without a user interface, enabling programmatic access to court records using PACER credentials.
  name: PACER Authentication API
- description: Court's electronic filing system (CM/ECF) for filing and managing case documents. Provides XML tags and NextGen CM/ECF integration.
  name: CM/ECF Electronic Filing
- description: Free public access to all Federal Circuit opinions, orders, and judgments published from October 2004 to present in PDF format.
  name: Online Opinions and Orders
- description: Online calendar of scheduled oral argument cases and courtroom assignments at the Federal Circuit.
  name: Scheduled Cases Calendar
- description: Aggregated case statistics and reports available through the court's media and public information pages, plus data request process.
  name: Statistical Reports
finops:
- name: Us Court Of Appeals For The Federal Circuit Finops
  service_category: API
  slug: us-court-of-appeals-for-the-federal-circuit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-court-of-appeals-for-the-federal-circuit.png
integrations:
- description: Federal Circuit case records fully integrated with the nationwide PACER federal court records system and CM/ECF filing system.
  name: PACER System
- description: Free Law Project's CourtListener provides API access to Federal Circuit opinions and RECAP-archived PACER documents.
  name: CourtListener
- description: Justia aggregates Federal Circuit case docket information and provides public access to filings.
  name: Justia Dockets
json_schemas:
- name: FederalCircuitCase
  property_count: 11
  slug: cafc-case
- name: DocketEntry
  property_count: 9
  slug: cafc-docket-entry
- name: FederalCircuitOpinion
  property_count: 10
  slug: cafc-opinion
json_structures:
- name: Cafc Case Structure
  property_count: 11
  slug: cafc-case-structure
- name: Cafc Docket Entry Structure
  property_count: 9
  slug: cafc-docket-entry-structure
- name: Cafc Opinion Structure
  property_count: 10
  slug: cafc-opinion-structure
jsonld:
- class_count: 5
  name: Us Court Of Appeals For The Federal Circuit Context
  property_count: 25
  slug: us-court-of-appeals-for-the-federal-circuit-context
layout: provider
modified: '2026-05-03'
name: US Court of Appeals for the Federal Circuit
nav: Providers
network: true
overview: 'US Court of Appeals for the Federal Circuit publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Legal, Patent Law, Federal Courts, and Appellate Courts.


  The US Court of Appeals for the Federal Circuit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Court of Appeals for the Federal Circuit''s developer surface includes engineering blog, documentation, getting-started guide, API reference, and 8 more developer resources.'
plans:
- name: Us Court Of Appeals For The Federal Circuit Plans Pricing
  plan_count: 3
  slug: us-court-of-appeals-for-the-federal-circuit-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Us Court Of Appeals For The Federal Circuit Rate Limits
  slug: us-court-of-appeals-for-the-federal-circuit-rate-limits
rules:
- name: US Court of Appeals for the Federal Circuit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-court-of-appeals-for-the-federal-circuit-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.9
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 46.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/us-court-of-appeals-for-the-federal-circuit/refs/heads/main/screenshots/us-court-of-appeals-for-the-federal-circuit-2026-06-20T200611.png
security:
- kind: domain-security
  name: Us Court Of Appeals For The Federal Circuit Domain Security
  slug: us-court-of-appeals-for-the-federal-circuit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: us-court-of-appeals-for-the-federal-circuit
tags:
- Federal Government
- Legal
- Patent Law
- Federal Courts
- Appellate Courts
use_cases:
- description: Researching Federal Circuit patent law precedent using published opinions, orders, and PACER case dockets.
  name: Patent Case Legal Research
- description: Finding Federal Circuit decisions on government contracts, federal employment, veterans benefits, and specialized federal jurisdiction.
  name: Federal Employment and Veterans Claims Research
- description: Programmatic access to Federal Circuit case dockets, filings, and documents using the PACER Authentication API and Case Locator API.
  name: Court Records Access via PACER
- description: Monitoring active Federal Circuit cases, oral arguments, and new opinions relevant to specific technology, trade, or legal areas.
  name: Appellate Monitoring
- description: Using PACER data to analyze trends in Federal Circuit patent, trade, and government contract decisions for legal research.
  name: Legal Data Analytics
website: https://www.cafc.uscourts.gov/
---
