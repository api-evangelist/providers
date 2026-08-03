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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amicus-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amicusrx.com
- group: company
  title: ''
  type: About
  url: https://www.amicusrx.com/about-amicus/
- group: other
  title: ''
  type: Products
  url: https://www.amicusrx.com/our-medicines/
- group: other
  title: ''
  type: Pipeline
  url: https://www.amicusrx.com/our-research-and-pipeline/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://www.amicusrx.com/our-research-and-pipeline/clinical-trials/
- group: other
  title: ''
  type: ExpandedAccess
  url: https://www.amicusrx.com/our-research-and-pipeline/expanded-access-program/
- group: other
  title: ''
  type: PatientAdvocacy
  url: https://www.amicusrx.com/for-patients/patient-advocacy/
- group: other
  title: ''
  type: ProductSite
  url: https://www.galafold.com
- group: other
  title: ''
  type: ProductSite
  url: https://www.pombilitiopfolda.com
- group: other
  title: ''
  type: ParentCompany
  url: https://www.biomarin.com
- group: company
  title: ''
  type: Investors
  url: https://investors.biomarin.com/
- group: company
  title: ''
  type: Careers
  url: https://www.biomarin.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amicus-therapeutics
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amicus-therapeutics/refs/heads/main/vocabulary/amicus-therapeutics-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amicus-therapeutics/refs/heads/main/json-ld/amicus-therapeutics-context.jsonld
description: 'Amicus Therapeutics is a global rare disease biotechnology company focused on discovering, developing, and commercializing medicines for people living with genetically defined conditions. Founded in 2002 and headquartered in Princeton, New Jersey, Amicus markets two approved therapies: Galafold (migalastat) — the first and only oral therapy for adults with Fabry disease who have an amenable GLA variant, approved by the European Commission in May 2016 — and the two-component Pombiliti (cipaglucosidase alfa-atga) + Opfolda (miglustat) enzyme replacement / stabilizer combination for adults with late-onset Pompe disease. Amicus operates wholly owned subsidiaries in Australia, Canada, France, Germany, Italy, Japan, the Netherlands, Spain, Switzerland, and the United Kingdom. BioMarin Pharmaceutical Inc. agreed to acquire Amicus in December 2025 for $4.8 billion; the acquisition completed on April 27, 2026 and Amicus now operates as a wholly owned subsidiary of BioMarin, having previously
  traded on NASDAQ under the ticker FOLD. The company maintains no publicly documented commercial developer APIs, SDKs, or GitHub organization; its digital surface is composed of corporate, product, patient-support, and clinical-trial websites.'
examples:
- key_count: 2
  name: Amicus Galafold Medicine Example
  slug: amicus-galafold-medicine-example
- key_count: 2
  name: Amicus Pombiliti Medicine Example
  slug: amicus-pombiliti-medicine-example
- key_count: 2
  name: Amicus Rossella Trial Example
  slug: amicus-rossella-trial-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amicus-therapeutics.png
json_schemas:
- name: Amicus Clinical Trial
  property_count: 10
  slug: amicus-clinical-trial
- name: Amicus Medicine
  property_count: 11
  slug: amicus-medicine
json_structures:
- name: Amicus Clinical Trial Structure
  property_count: 0
  slug: amicus-clinical-trial-structure
- name: Amicus Medicine Structure
  property_count: 0
  slug: amicus-medicine-structure
jsonld:
- class_count: 32
  name: Amicus Therapeutics Context
  property_count: 4
  slug: amicus-therapeutics-context
layout: provider
modified: '2026-05-23'
name: amicus-therapeutics
nav: Providers
network: true
overview: 'amicus-therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Rare Diseases, Genetic Diseases, and Fabry Disease.


  The amicus-therapeutics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 84
rules:
- name: amicus-therapeutics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amicus-therapeutics-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 44.4
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amicus-therapeutics/refs/heads/main/screenshots/amicus-therapeutics-2026-06-20T171931.png
security:
- kind: domain-security
  name: Amicus Therapeutics Domain Security
  slug: amicus-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amicus-therapeutics
tags:
- Biotechnology
- Pharmaceuticals
- Rare Diseases
- Genetic Diseases
- Fabry Disease
- Pompe Disease
- Lysosomal Storage Disorders
- Enzyme Replacement Therapy
- Pharmacological Chaperones
- Clinical Research
- Life Sciences
- Patient Advocacy
website: https://www.amicusrx.com
---
