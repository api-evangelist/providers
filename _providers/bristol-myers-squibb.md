---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: BMS Medical Information Online provides US healthcare providers with prescribing information, medical inquiry submission, and product/regimen libraries for BMS medicines across oncology, hematology, i
  name: BMS Medical Information Portal
  slug: medical-information-api
- description: BMS Clinical Trials is the clinical trial search and enrollment platform for patients and caregivers looking for Bristol Myers Squibb sponsored studies. It was formerly published as BMS Study Connect;
  name: BMS Study Connect
  slug: study-connect
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bristol-myers-squibb-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BristolMyersSquibb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bristol-myers-squibb
- group: company
  title: ''
  type: Website
  url: https://www.bms.com
- group: other
  title: ''
  type: x-ResearchDataSharing
  url: https://www.bms.com/research-and-development/independent-research/data-sharing-request-process.html
- group: other
  title: ''
  type: x-BusinessDevelopment
  url: https://www.bms.com/our-company/partnerships-and-business-development.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.bms.com
- group: build
  title: ''
  type: Packages
  url: packages/bristol-myers-squibb-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bristol-myers-squibb-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bristol-myers-squibb-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/bristol-myers-squibb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bristol-myers-squibb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bristol-myers-squibb-finops.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bms.com/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bms.com/legal-notice.html
- group: company
  title: ''
  type: Blog
  url: https://www.bms.com/life-and-science.html
- group: start
  title: ''
  type: x-ClinicalTrials
  url: https://www.bms.com/research-and-development/clinical-trials.html
created: '2026-03-21'
description: Bristol Myers Squibb (BMS) is a global Fortune 500 biopharmaceutical company committed to discovering, developing, and delivering innovative medicines for patients with serious diseases. BMS focuses on oncology, immunology, cardiovascular, fibrosis, and cell therapy (CAR T). The company operates BMS Study Connect for clinical trial recruitment, a Medical Information portal for healthcare providers, and the BMS Business Development platform for research partnerships and data sharing. BMS actively pursues technology partnerships in protein degradation, advanced treatment modalities, and digital health.
finops:
- name: Bristol Myers Squibb Finops
  service_category: Pharmaceutical
  slug: bristol-myers-squibb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bristol-myers-squibb.png
layout: provider
modified: '2026-09-04'
name: Bristol Myers Squibb
nav: Providers
network: true
overview: 'Bristol Myers Squibb publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Biopharmaceutical, Oncology, Immunology, and Cardiovascular.


  Bristol Myers Squibb''s developer surface includes engineering blog and 16 more developer resources.'
plans:
- name: Bristol Myers Squibb Plans Pricing
  plan_count: 0
  slug: bristol-myers-squibb-plans-pricing
press:
- date: '2026-05-25'
  title: 'Science Firsthand: Predicting new possibilities in drug ...'
  url: https://www.bms.com/life-and-science/science/predictive-molecule-invention.html
- date: '2026-05-25'
  title: Corporate news details
  url: https://news.bms.com/news/details/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx
- date: '2026-05-25'
  title: Tempus Expands Strategic Collaboration with Bristol Myers ...
  url: https://www.tempus.com/news/pr/tempus-expands-strategic-collaboration-with-bristol-myers-squibb-to-enhance-the-probability-of-success-across-clinical-development-programs-in-oncology-and-neuroscience/?srsltid=AfmBOopP82Z39HypdcQ5atFZGKjb7FN-dLZrhJlFnEOjfYJoRTGxSec5
- date: '2026-05-25'
  title: Evinova, Bristol Myers Squibb Partner to Apply AI to Global ...
  url: https://www.appliedclinicaltrialsonline.com/view/evinova-bristol-myers-squibb-partner-ai-global-clinical-development
- date: '2026-05-25'
  title: Our technologies
  url: https://www.bms.com/about-us/our-company/our-technologies.html
random_paper: 5
rate_limits:
- limit_count: 0
  name: Bristol Myers Squibb Rate Limits
  slug: bristol-myers-squibb-rate-limits
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bristol-myers-squibb/refs/heads/main/screenshots/bristol-myers-squibb-2026-06-20T173708.png
security:
- kind: domain-security
  name: Bristol Myers Squibb Domain Security
  slug: bristol-myers-squibb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bristol-myers-squibb
tags:
- Pharmaceuticals
- Biopharmaceutical
- Oncology
- Immunology
- Cardiovascular
- Clinical Trials
- Digital Health
- Fortune 500
website: https://www.bms.com
---
