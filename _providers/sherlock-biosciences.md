---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-27'
  detail: Sherlock Biosciences was acquired by OraSure Technologies in December 2024 and fully absorbed; its own domain sherlock.bio now returns a bare 301 to orasure.com, and every contract-discovery and .well-known path probed on sherlock.bio, orasure.com and www.orasure.com returned 404, leaving a molecular-diagnostics company that never ran a developer program with no surviving API surface of any kind.
  evidence:
  - status: 301
    url: https://sherlock.bio/
  - status: 404
    url: https://sherlock.bio/openapi.json
  - status: 404
    url: https://sherlock.bio/.well-known/agent-card.json
  - status: 404
    url: https://orasure.com/openapi.json
  - status: 404
    url: https://www.orasure.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/SherlockBiosciences
  reason: defunct
  state: none
created: '2026-08-27'
description: Sherlock Biosciences is a molecular diagnostics company founded in 2019 out of the Broad Institute to commercialize SHERLOCK (Specific High-sensitivity Enzymatic Reporter unLOCKing), the CRISPR-based nucleic-acid detection method developed in the Zhang lab, alongside INSPECTR, an ambient-temperature synthetic-biology amplification platform. In May 2020 it received the first FDA Emergency Use Authorization ever granted to a CRISPR-based diagnostic, for SARS-CoV-2. The company developed disposable, instrument-free molecular self-tests, led by a combined Chlamydia trachomatis and Neisseria gonorrhoeae assay. OraSure Technologies acquired Sherlock Biosciences in December 2024 and absorbed it into its rapid-diagnostics portfolio; the sherlock.bio domain now permanently redirects to orasure.com. Sherlock Biosciences is a laboratory diagnostics developer and has never operated a public developer program, HTTP API, or machine-readable API contract.
layout: provider
modified: '2026-08-27'
name: Sherlock Biosciences
nav: Providers
network: true
random_paper: 5
slug: sherlock-biosciences
tags:
- Diagnostics
- Molecular Diagnostics
- CRISPR
- Biotechnology
- Life Sciences
- Healthcare
- Infectious Disease
- Point of Care Testing
- Synthetic Biology
- Bioinformatics
- Acquired
---
