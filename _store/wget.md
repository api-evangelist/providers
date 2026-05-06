---
aid: wget
name: Wget
description: GNU Wget is a free, open-source command-line utility for non-interactive downloading of files from the web using HTTP, HTTPS, FTP, and FTPS protocols. It supports recursive downloading, resuming aborted downloads, mirroring websites, proxy support, and can be run from scripts and cron jobs. Wget2 is the next-generation successor, written from scratch with multi-threading, HTTP/2, and a plugin API via libwget.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CLI
  - Clients
  - HTTP Client
  - File Download
  - Open Source
  - GNU
url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wget:wget
    name: Wget
    description: GNU Wget is a free command-line utility for non-interactive downloading of files from the web using HTTP, HTTPS, FTP, and FTPS. It supports recursive downloading, resume of aborted downloads, website mirroring, HTTP proxies, cookies, and persistent connections.
    humanURL: https://www.gnu.org/software/wget/
    baseURL: https://ftp.gnu.org/gnu/wget/
    tags:
      - CLI
      - File Download
      - HTTP Client
      - FTP Client
      - GNU
      - Open Source
    properties:
      - type: Documentation
        url: https://www.gnu.org/software/wget/manual/
      - type: Getting Started
        url: https://www.gnu.org/software/wget/manual/wget.html
      - type: Download
        url: https://ftp.gnu.org/gnu/wget/
      - type: Mirror
        url: http://ftpmirror.gnu.org/wget
      - type: Source Code
        url: https://git.savannah.gnu.org/cgit/wget.git
      - type: Bug Tracker
        url: https://savannah.gnu.org/bugs/?group=wget
      - type: Mailing List
        url: https://lists.gnu.org/mailman/listinfo/bug-wget
      - type: FAQ
        url: http://wget.addictivecode.org/FrequentlyAskedQuestions
    contact:
      - FN: GNU Wget Mailing List
        email: bug-wget@gnu.org
  - aid: wget:wget2
    name: Wget2
    description: GNU Wget2 is the next-generation successor to GNU Wget, built from scratch around libwget. It is multi-threaded, supports HTTP/2, HTTP compression, parallel connections, If-Modified-Since headers, plugin APIs, RSS/Atom feed scanning, Sitemap XML support, and Metalink. Libwget is licensed under LGPLv3+ for use as a reusable library.
    humanURL: https://gitlab.com/gnuwget/wget2
    baseURL: https://gnuwget.gitlab.io/wget2/
    tags:
      - CLI
      - File Download
      - HTTP Client
      - HTTP/2
      - Multithreaded
      - Plugin API
      - GNU
      - Open Source
    properties:
      - type: Documentation
        url: https://gnuwget.gitlab.io/wget2/reference/
      - type: Source Code
        url: https://gitlab.com/gnuwget/wget2
      - type: GitHub Mirror
        url: https://github.com/gnuwget/wget2
      - type: Plugin API
        url: https://gnuwget.gitlab.io/wget2/reference/group__libwget-plugin.html
      - type: Releases
        url: https://gitlab.com/gnuwget/wget2/-/releases
      - type: Wiki
        url: https://gitlab.com/gnuwget/wget2/-/wikis/home
      - type: ChangeLog
        url: https://fossies.org/linux/wget/ChangeLog
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/json-schema/wget-download-request-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/json-schema/wget2-plugin-schema.json
    contact:
      - FN: GNU Wget Mailing List
        email: bug-wget@gnu.org
common:
  - type: Website
    url: https://www.gnu.org/software/wget/
  - type: Documentation
    url: https://www.gnu.org/software/wget/manual/
  - type: Source Code
    url: https://git.savannah.gnu.org/cgit/wget.git
  - type: GitHub Organization
    url: https://gitlab.com/gnuwget
  - type: Mailing List
    url: https://lists.gnu.org/mailman/listinfo/bug-wget
  - type: Bug Tracker
    url: https://savannah.gnu.org/bugs/?group=wget
  - type: Download
    url: https://ftp.gnu.org/gnu/wget/
  - type: License
    url: https://www.gnu.org/licenses/gpl-3.0.html
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/vocabulary/wget-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/wget/refs/heads/main/json-ld/wget-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
