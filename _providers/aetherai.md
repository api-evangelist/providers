---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: aetherAI sells FDA-cleared digital-pathology software (aetherSlide, aetherWeb, Hema, Endo, Ortho) only as an end-user clinical product — there is no developer program, no developer portal, no OpenAPI and no API documentation on any host, and the DPAI application at demo.aetherai.com is a login-walled single-page app whose /api/, /openapi.json and /api/schema/ paths all return 404 to an anonymous client; the only callable public endpoint is the Wix platform's site MCP at www.aetherai.com/_api/mcp, which serves marketing-site content rather than any clinical product.
  evidence:
  - status: 400
    url: https://www.aetherai.com/openapi.json
  - status: 404
    url: https://demo.aetherai.com/openapi.json
  - status: 404
    url: https://demo.aetherai.com/api/
  - status: 200
    url: https://www.aetherai.com/products
  - status: 200
    url: https://www.aetherai.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'aetherAI (雲象科技, aetherAI Co., Ltd.) is a Taipei-based medical-imaging AI company and one of Asia''s leading digital-pathology vendors. It builds regulated diagnostic software for hospitals, reference laboratories and pharmaceutical R&D: aetherSlide, an FDA-cleared (K233126), CE-marked and TFDA-approved whole-slide image management and viewing system; aetherWeb, a cloud digital pathology education platform; aetherAI Hema for bone-marrow smear differential counting; aetherAI Endo for real-time computer-aided polyp detection in colonoscopy; and aetherAI Ortho for whole-spine radiograph measurement. The company was founded in Taiwan, raised NT$765 million in Series B funding led by CDIB Capital, Quanta Computer, Taiwan Business Bank VC and Cathay Venture, listed on Taiwan''s Emerging Stock Board in November 2024, holds ISO/IEC 27001 certification, and has filed for the Taiwan Innovation Board. aetherAI publishes no public developer API, no OpenAPI or other machine-readable contract,
  and no developer portal; its clinical software is sold and deployed through a direct enterprise motion and its application sits behind a customer login. The single publicly callable surface is a Wix-provided Site MCP endpoint on its own domain, which serves website content rather than any clinical product.'
image: https://static.wixstatic.com/media/5feca6_8ade720b19a64d2fb13934d0ad55a0b9~mv2.jpg/v1/fill/w_2500,h_1600,al_c/5feca6_8ade720b19a64d2fb13934d0ad55a0b9~mv2.jpg
layout: provider
modified: '2026-09-12'
name: aetherAI
nav: Providers
network: true
random_paper: 16
slug: aetherai
tags:
- Healthcare
- Digital Pathology
- Medical Imaging
- Artificial Intelligence
- Diagnostics
- Machine Learning
- Medical Devices
- Life Sciences
- MCP
- Taiwan
---
