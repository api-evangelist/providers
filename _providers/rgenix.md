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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rgenix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inspirna.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inspirna.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inspirna.com/terms-of-use/
coverage:
  checked: '2026-08-26'
  detail: Rgenix is a clinical-stage oncology drug developer that renamed itself Inspirna in September 2021; rgenix.com now 301s to an unresponsive www.rgenix.com, and the live corporate site inspirna.com is a WordPress marketing site (company/science/pipeline/patients/careers/news) with no developer section, no GitHub organization, and a 404 on every contract-discovery path.
  evidence:
  - status: 404
    url: https://inspirna.com/openapi.json
  - status: 404
    url: https://inspirna.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/inspirna
  - status: 301
    url: http://rgenix.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Rgenix, Inc. is a clinical-stage biopharmaceutical company founded by scientists from The Rockefeller University to discover and develop first-in-class small molecules and biologics against previously undruggable drivers of cancer metastasis, using its proprietary RNA-DRIVEr target-discovery platform. Its programs include ompenaclid (RGX-202), an oral SLC6A8/creatine-transporter inhibitor in Phase 2 for RAS-mutant colorectal cancer, abequolixron (RGX-104), an oral LXR agonist in Phase 1b/2, and RGX-019-MMAE, a MERTK-targeting antibody-drug conjugate. The company changed its corporate name from Rgenix to Inspirna in September 2021 and operates from Long Island City, New York. It is a therapeutics developer with no public API, developer program, or machine-readable interface.
layout: provider
modified: '2026-08-26'
name: Rgenix
nav: Providers
network: true
overview: Rgenix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Drug Discovery.
random_paper: 2
security:
- kind: domain-security
  name: Rgenix Domain Security
  slug: rgenix-domain-security
  summary_line: TLSv1.3
slug: rgenix
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Drug Discovery
- Clinical Trials
- Life Sciences
website: https://inspirna.com/
---
