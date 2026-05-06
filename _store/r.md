---
aid: r
name: R
description: R is a free, open-source programming language and statistical computing environment maintained by the R Core Team and supported by the R Foundation. It provides a wide variety of statistical and graphical techniques and is highly extensible through its package ecosystem on CRAN (Comprehensive R Archive Network), Bioconductor, and GitHub. R is widely used among statisticians, data scientists, and researchers for data analysis, visualization, and reproducible research.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/r/refs/heads/main/apis.yml
tags:
  - R
  - Statistics
  - Data Science
  - Open Source
  - Programming Language
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: r:metacran-crandb
    name: METACRAN CranDB API
    description: CouchDB-based REST API providing programmatic access to metadata for all CRAN R packages. Supports package lookup, version history, and package dependency data in JSON format.
    humanURL: https://github.com/metacran/crandb
    baseURL: https://crandb.r-pkg.org
    tags:
      - CRAN
      - Packages
      - Metadata
    properties:
      - type: Documentation
        url: https://github.com/metacran/crandb
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/r/refs/heads/main/openapi/r-metacran-crandb-openapi.yml
  - aid: r:metacran-cranlogs
    name: METACRAN CranLogs API
    description: REST API providing download statistics for R packages from the RStudio CRAN mirror. Supports daily, weekly, monthly, and grand-total download counts with badge generation endpoints.
    humanURL: https://github.com/metacran/cranlogs.app
    baseURL: https://cranlogs.r-pkg.org
    tags:
      - CRAN
      - Downloads
      - Statistics
    properties:
      - type: Documentation
        url: https://github.com/metacran/cranlogs.app
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/r/refs/heads/main/openapi/r-metacran-cranlogs-openapi.yml
  - aid: r:rversions
    name: R Versions API
    description: REST API that reports the current and previous stable releases of R, including version numbers and release dates. Used by CI tools and package managers to determine supported R versions.
    humanURL: https://github.com/metacran/rversions.app
    baseURL: https://rversions.r-pkg.org
    tags:
      - R
      - Versions
      - Releases
    properties:
      - type: Documentation
        url: https://github.com/metacran/rversions.app
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/r/refs/heads/main/openapi/r-rversions-openapi.yml
common:
  - type: Website
    url: https://www.r-project.org/
  - type: Documentation
    url: https://cran.r-project.org/manuals.html
  - type: GitHubOrg
    url: https://github.com/r-lib
  - type: GitHubOrg
    url: https://github.com/r-devel
  - type: PackageRegistry
    url: https://cran.r-project.org/
  - type: PackageRegistry
    url: https://bioconductor.org/
  - type: PackageSearch
    url: https://www.rdocumentation.org/
  - type: PackageSearch
    url: https://rdrr.io/
  - type: Blog
    url: https://blog.r-project.org/
  - type: Forum
    url: https://stat.ethz.ch/mailman/listinfo/r-help
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/r
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
