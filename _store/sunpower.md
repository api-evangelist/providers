---
aid: sunpower
name: SunPower
description: 'SunPower is a residential solar energy company (Nasdaq: SPWR) that designs, installs, and finances solar systems and battery storage for homeowners. The original SunPower Corporation filed for Chapter 11 bankruptcy in August 2024; its assets were acquired by Complete Solaria in September 2024, which rebranded as SunPower Inc. in April 2025. SunPower maintains the GitHub org github.com/SunPower, hosting open-source solar modeling tools including pvfactors (view-factor model for bifacial PV modeling), PVMismatch (mismatch loss calculations), and SolarUtils. These Python libraries are used by solar energy professionals and researchers for photovoltaic system modeling and simulation.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Solar Energy
  - Renewable Energy
  - Photovoltaics
  - Open Source
  - Python
url: https://raw.githubusercontent.com/api-evangelist/sunpower/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sunpower:pvfactors
    name: pvfactors
    description: pvfactors is an open-source Python library for modeling diffuse shading and bifacial photovoltaic (PV) irradiance. It implements 2D geometry and view-factor mathematics to account for reflections between array surfaces including front and back sides of bifacial modules, ground, and sky. Used by PV professionals for simulation of complex shading scenarios, time-series irradiance calculations, and energy yield assessment. Maintained under the SunPower GitHub organization.
    humanURL: https://github.com/SunPower/pvfactors
    tags:
      - Solar Energy
      - Photovoltaics
      - Irradiance Modeling
      - Bifacial PV
      - Python
      - Open Source
    properties:
      - type: Documentation
        url: https://sunpower.github.io/pvfactors/
      - type: GitHub
        url: https://github.com/SunPower/pvfactors
      - type: PyPI
        url: https://pypi.org/project/pvfactors/
  - aid: sunpower:pvmismatch
    name: PVMismatch
    description: PVMismatch is an open-source Python library for calculating mismatch losses in photovoltaic systems. It models I-V and P-V curves for PV cells, modules, and strings to quantify power loss from cell-to-cell or module-to-module variation in electrical characteristics.
    humanURL: https://github.com/SunPower/PVMismatch
    tags:
      - Solar Energy
      - Photovoltaics
      - Mismatch Loss
      - Python
      - Open Source
    properties:
      - type: GitHub
        url: https://github.com/SunPower/PVMismatch
  - aid: sunpower:solar-utils
    name: SolarUtils
    description: SolarUtils is an open-source Python package providing solar position algorithms and utility functions for solar energy calculations, including sun position (azimuth, elevation, zenith), sunrise/sunset times, and solar irradiance decomposition models.
    humanURL: https://github.com/SunPower/SolarUtils
    tags:
      - Solar Energy
      - Solar Position
      - Irradiance
      - Python
      - Open Source
    properties:
      - type: GitHub
        url: https://github.com/SunPower/SolarUtils
common:
  - type: Website
    url: https://www.sunpower.com
  - type: GitHub Organization
    url: https://github.com/SunPower
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
