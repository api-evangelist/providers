---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: BEKhealth runs a real documentation portal at docs.bekhealth.com, but every path on it — the root, /openapi.json, /llms.txt, even /.well-known/agent-card.json — returns a 302 into the company's Auth0 tenant at auth.bekhealth.com, so the contract is readable only by an existing customer with a signed BAA/DUA; nothing on the public marketing site names an API at all.
  evidence:
  - status: 302
    url: https://docs.bekhealth.com/
  - status: 302
    url: https://docs.bekhealth.com/openapi.json
  - status: 404
    url: https://api.bekhealth.com/openapi.json
  - status: 404
    url: https://www.bekhealth.com/.well-known/agent-card.json
  - status: 200
    url: https://www.bekhealth.com/llms.txt
  - status: 200
    url: https://auth.bekhealth.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: BEKhealth is a clinical research technology company whose BEKplatform applies a BERT-based deep-learning model to structured and unstructured electronic health record data — physician notes, pathology reports, clinical endpoints — to power trial feasibility, patient matching and research-grade real-world data for sponsors, CROs and research site networks. The company markets 25+ proprietary EHR adapters reaching roughly 80% of the EHR market (Epic, Cerner, athenahealth, NextGen, eClinicalWorks, Veradigm, Greenway, ModMed, DrChrono, Elation, AdvancedMD, Flatiron, OpenEMR and others), a longitudinal patient graph mapped to an ontology of more than 24 million clinical terms, and the BEKnetwork of 200+ research sites covering 30M+ patient records. Delivery is enterprise SaaS — sold direct and through AWS Marketplace, and embedded in partner platforms such as CRIO eSource/CTMS. BEKhealth operates a documentation portal at docs.bekhealth.com and an Auth0 OpenID Connect issuer at auth.bekhealth.com,
  but publishes no public developer portal, API reference or machine-readable specification; the documented route to the platform is a demo request and a contracted onboarding with BAAs and DUAs.
image: https://www.bekhealth.com/wp-content/uploads/2025/02/BEKhealth_Logo-1.webp
layout: provider
modified: '2026-08-06'
name: BEKHealth
nav: Providers
network: true
random_paper: 32
slug: bekhealth
tags:
- Company
- Healthcare
- Clinical Trials
- Clinical Research
- Electronic Health Records
- Real World Data
- Artificial Intelligence
- Patient Recruitment
- Life Sciences
- Health Data
---
