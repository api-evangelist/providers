---
aid: pypi
name: PyPI
description: PyPI (Python Package Index) is the official third-party software repository for Python, serving as the central hub where developers publish and distribute Python packages. Their developer platform provides a suite of APIs for querying package metadata, downloading distributions, publishing packages, verifying supply chain integrity, and tracking download statistics across the Python ecosystem.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Open Source
  - Package Management
  - Packages
  - Python
url: https://raw.githubusercontent.com/api-evangelist/pypi/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: pypi:json
    name: PyPI JSON API
    description: The PyPI JSON API provides metadata about individual Python packages hosted on the Python Package Index. It returns project-level information including the latest version, all available releases, download URLs, and hash digests for MD5, SHA256, and BLAKE2b-256. Developers can query endpoints like /pypi/{project}/json for the latest release metadata or /pypi/{project}/{version}/json for a specific version. Responses are cached by CDN and support ETag headers for conditional requests.
    humanURL: https://docs.pypi.org/api/json/
    tags:
      - Metadata
      - Open Source
      - Packages
      - Python
    properties:
      - type: Documentation
        url: https://docs.pypi.org/api/json/
      - type: OpenAPI
        url: openapi/pypi-json-api-openapi.yml
  - aid: pypi:index
    name: PyPI Index API
    description: The PyPI Index API implements the PEP 503 (HTML) and PEP 691 (JSON) simple repository standards for discovering and downloading Python packages. It provides a machine-readable index of all registered projects and their available distribution files. The API is available in both HTML and JSON formats, with JSON recommended for new integrations. This is the primary API that package installers like pip use to resolve and download dependencies from the Python Package Index.
    humanURL: https://docs.pypi.org/api/index-api/
    tags:
      - Index
      - Packages
      - PEP 503
      - PEP 691
      - Python
    properties:
      - type: Documentation
        url: https://docs.pypi.org/api/index-api/
      - type: OpenAPI
        url: openapi/pypi-index-api-openapi.yml
  - aid: pypi:integrity
    name: PyPI Integrity API
    description: The PyPI Integrity API provides access to digital attestations and provenance information for Python package distribution files. It allows clients to retrieve cryptographic attestation bundles and Trusted Publishing metadata for individual release files, enabling verification of package authenticity and supply chain integrity. The API implements PEP 740 and returns provenance objects containing one or more Sigstore attestation bundles along with the identity that produced them. This endpoint is currently available in JSON format only.
    humanURL: https://docs.pypi.org/api/integrity/
    tags:
      - Attestations
      - Provenance
      - Python
      - Security
      - Supply Chain
    properties:
      - type: Documentation
        url: https://docs.pypi.org/api/integrity/
      - type: OpenAPI
        url: openapi/pypi-integrity-api-openapi.yml
  - aid: pypi:upload
    name: PyPI Upload API
    description: The PyPI Upload API is the endpoint used by tools like twine and build frontends to publish Python package distributions to the Python Package Index. Served at upload.pypi.org, it emulates the legacy PyPI upload interface and accepts source distributions and wheel files along with their metadata. The API also supports attaching PEP 740 digital attestations to uploads, which PyPI will verify before accepting. Authentication is handled via API tokens or Trusted Publishing workflows using OpenID Connect.
    humanURL: https://docs.pypi.org/api/upload/
    tags:
      - Packages
      - Publishing
      - Python
      - Upload
    properties:
      - type: Documentation
        url: https://docs.pypi.org/api/upload/
      - type: OpenAPI
        url: openapi/pypi-upload-api-openapi.yml
  - aid: pypi:feeds
    name: PyPI RSS Feeds
    description: 'PyPI provides RSS feeds that allow developers and tools to monitor package activity on the Python Package Index. Three feeds are available: the Newest Packages feed for recently registered projects, the Latest Updates feed for the most recently updated projects, and per-project release feeds for tracking new versions of specific packages. These feeds enable integration with feed readers, monitoring tools, and automation workflows to stay informed about Python package ecosystem changes.'
    humanURL: https://docs.pypi.org/api/feeds/
    tags:
      - Feeds
      - Packages
      - Python
      - RSS
      - Updates
    properties:
      - type: Documentation
        url: https://docs.pypi.org/api/feeds/
  - aid: pypi:stats
    name: PyPI Stats API
    description: The PyPI Stats API provides aggregate download statistics and time series data for Python packages hosted on PyPI. It offers JSON endpoints for querying download counts broken down by Python version, operating system, and time period. Time series data is retained for 180 days and all download statistics are updated once daily. The API is hosted at pypistats.org and serves as the primary programmatic interface for analyzing Python package adoption and download trends across the ecosystem.
    humanURL: https://pypistats.org/api/
    tags:
      - Analytics
      - Downloads
      - Packages
      - Python
      - Statistics
    properties:
      - type: Documentation
        url: https://pypistats.org/api/
      - type: OpenAPI
        url: openapi/pypi-stats-api-openapi.yml
common:
  - type: Portal
    url: https://docs.pypi.org/
  - type: Documentation
    url: https://docs.pypi.org/api/
  - type: Website
    url: https://pypi.org/
  - type: PrivacyPolicy
    url: https://policies.python.org/pypi.org/Privacy-Policy/
  - type: TermsOfService
    url: https://policies.python.org/pypi.org/Terms-of-Use/
  - type: Support
    url: https://pypi.org/help/
  - type: Blog
    url: https://blog.pypi.org/
  - type: Login
    url: https://pypi.org/account/login/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
