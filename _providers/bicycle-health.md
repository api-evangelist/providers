---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Bicycle Health is a virtual OUD clinic, not a software vendor — its patient app is served by a private Express backend at api.bicyclehealth.com (GET / returns "Cannot GET /", GET /health returns 204) that publishes no spec, no docs host, and no developer program of any kind; the only machine-readable thing it ships is a patient-facing llms.txt for AI answer engines.
  evidence:
  - status: 204
    url: https://api.bicyclehealth.com/health
  - status: 404
    url: https://api.bicyclehealth.com/openapi.json
  - status: 0
    url: https://developers.bicyclehealth.com/
  - status: 404
    url: https://www.bicyclehealth.com/developers
  - status: 404
    url: https://www.bicyclehealth.com/.well-known/agent-card.json
  - status: 200
    url: https://www.bicyclehealth.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'Bicycle Health is a US telehealth provider of Medication for Addiction Treatment (MAT) for opioid use disorder (OUD), founded in 2017 by Ankit Gupta in Redwood City, California and delivering virtual care since 2020. Care is delivered entirely by secure video visit — intake, provider visits, treatment planning and ongoing support — with prescriptions sent electronically to a pharmacy near the patient. Medications offered include buprenorphine/naloxone (Suboxone), monthly injectable buprenorphine (Sublocade), weekly or monthly injectable buprenorphine (Brixadi) and monthly injectable naltrexone (Vivitrol), and the company also treats kratom and 7-hydroxymitragynine (7-OH) dependence. Bicycle Health accepts most major insurers including Medicaid (in most states it operates in), Medicare and TRICARE, states it has helped over 55,000 patients across 25+ US states, and was named a TIME100 Most Influential Company in 2022 and a Fast Company Most Innovative Company in 2024. It is
  a clinical care organization rather than a software vendor: it ships a patient web and mobile application backed by a private API host, but publishes no public developer program, API documentation, SDK or machine-readable contract.'
image: https://cdn.prod.website-files.com/61f7c8145fe6f608faa84b36/624155b2363584ddcd78b1a5_opengraph.png
layout: provider
modified: '2026-08-07'
name: Bicycle Health
nav: Providers
network: true
random_paper: 50
slug: bicycle-health
tags:
- Company
- Health
- Healthcare
- Telehealth
- Digital Health
- Behavioral Health
- Addiction Treatment
- Opioid Use Disorder
- Medication for Addiction Treatment
- Virtual Care
---
