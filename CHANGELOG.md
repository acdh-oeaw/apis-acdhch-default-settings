# Changelog

## [2.6.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.5.0...v2.6.0) (2025-04-29)


### Features

* **settings:** add collections, history to INSTALLED_APPS ([48b01e0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/48b01e08cff206065802d21db8f7d6ac82f057f6)), closes [#197](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/197)

## [2.5.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.4.0...v2.5.0) (2025-04-14)


### Features

* **templates:** add a monitoring variable to the meta tags ([06a729d](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/06a729de0483ff208cf7f6021c64adae7830faf9))


### Documentation

* **settings:** drop unnecessary comment ([5db1d0a](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/5db1d0ad38bb724e28dd842d0605345c09395eac)), closes [#188](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/188)

## [2.4.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.3.1...v2.4.0) (2025-03-20)


### Features

* **querysets:** add ExternalAutocomplete for E53_Place and E21_Person ([acd27d1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/acd27d15fb4326fd4381de8963e8bbdf3b458a51))
* **settings:** set additional lookup module path ([dfe8d5c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/dfe8d5ca3a701cb825bcce3f94f75a5a78398004))

## [2.3.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.3.0...v2.3.1) (2025-02-28)


### Bug Fixes

* **settings:** add resources used by leaflet to CSP_IMG_SRC ([c931735](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/c931735c12684b1820cf30a8004aecf636a8cc59))

## [2.3.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.2.2...v2.3.0) (2025-02-28)


### Features

* **settings:** (re)add Content Security Policy setting ([686da51](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/686da519184c4a945f08f454614b003277d7df94))


### Bug Fixes

* **settings:** drop apis_vocabularies from INSTALLED_APPS ([899b2d8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/899b2d8b3806ee39b8db46bc5383edb8288901c8))

## [2.2.2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.2.1...v2.2.2) (2025-02-20)


### Bug Fixes

* **settings:** move generic app further up in the INSTALLED_APPS list ([142e900](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/142e9009e9fb537641578dbf656408c88ef16638))

## [2.2.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.2.0...v2.2.1) (2025-02-20)


### Bug Fixes

* **settings:** drop apis_override_select2js from INSTALLED_APPS ([e651b1b](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/e651b1b210eab55960fbe0eb264da202183b2287))

## [2.2.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.1.0...v2.2.0) (2025-02-18)


### Features

* **settings:** add `apis_core.relations` to INSTALLED_APPS ([bbbf42b](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/bbbf42bd60e29b4b8a6d12c5e893679d6b6446f1))
* **settings:** introduce a separate CSP setting for images ([ddf111f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ddf111f5e861d4e99d6c96a058c968460779ed77))


### Bug Fixes

* **settings:** set default tables2 template to bootstrap5-reponsive ([4c2fa2c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/4c2fa2c8385faeb16aaae0954bb53d5e60ae88cd)), closes [#167](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/167)

## [2.1.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v2.0.0...v2.1.0) (2025-02-05)


### Features

* **settings:** change default crispy & tables theme to bootstrap5 ([f1dfcfb](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/f1dfcfb40849fb28ef8ec92a1e3903f65b4eb400))

## [2.0.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.8.0...v2.0.0) (2025-01-29)


### ⚠ BREAKING CHANGES

* **settings:** drop apis_relations from INSTALLED_APPS

### Features

* **settings:** drop apis_relations from INSTALLED_APPS ([eeea767](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/eeea7671afa9435d7c5996117ff84e50b3354f33))


### Bug Fixes

* **settings:** drop deprecated USE_L10N setting ([7d1ee88](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7d1ee88caf9f51199eec9464c2e31b32ac33f9d2)), closes [#144](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/144)
* **settings:** remove unused third party sources from CSP settings ([3188782](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/318878244f1bab6cadb1d4f217efdb1c167323e8)), closes [#82](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/82)

## [1.8.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.7.0...v1.8.0) (2024-12-17)


### Features

* **deps:** add django-removals dependency and add it to installed apps ([d60dfbb](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d60dfbb6d8b47ed33c7a0cb54c1f38d4bb1b3d66)), closes [#122](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/122)
* **views:** replace utils with views ([ce4e839](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ce4e839f5108ac44cfa9e9a2a9ca8f5f6bafda92)), closes [#134](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/134)


### Bug Fixes

* **settings:** add HistoryRequestMiddleware ([7e66df2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7e66df2d103514535ac544fd9ed7f42746a7a590)), closes [#93](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/93)
* **settings:** replace os.path with pathlib.Path ([d0c77ba](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d0c77ba075a3ae25927c077f19cdbdecb6038998))
* **settings:** set DEFAULT_AUTO_FIELD ([1208d9c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1208d9c66c6145c0d463217f13b59592059ec6f9))

## [1.7.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.6.1...v1.7.0) (2024-12-03)


### Features

* **urls:** include staticfiles_urlpatterns in default urls ([19101c7](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/19101c71197728c25e2e0439f0e48e1dc184fcd2)), closes [#131](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/131)

## [1.6.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.6.0...v1.6.1) (2024-11-29)


### Bug Fixes

* **settings:** set `LOGIN_REDIRECT_URL` to `/` ([18eea29](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/18eea29d38320000661acbbd3bd5cd1d2f44d2fa))

## [1.6.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.5.0...v1.6.0) (2024-11-22)


### Features

* **settings:** point LOGIN_URL to the default APIS login route ([4866b48](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/4866b48d22f8f26ef5aa771950bd421d50f44bfe)), closes [#123](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/123)


### Documentation

* **settings:** point all Django documentation links to stable docs ([e08771a](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/e08771a7f78466a8ddefd4c0618fbc907540f7f7))

## [1.5.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.4.0...v1.5.0) (2024-11-06)


### Features

* **settings:** allow to set DEBUG from environment ([1677bf4](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1677bf4b9bce8c1dc7f62f8c1f6ac400917dbd69))


### Bug Fixes

* **urls:** drop inclusion of webpage app in urls ([fb3947c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/fb3947c85ba711723b72453df7ebe7db8f9a189b)), closes [#114](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/114)

## [1.4.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.3.0...v1.4.0) (2024-10-18)


### Features

* **deps:** add opentelemetry dependencies ([845b4b2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/845b4b24c79d66f0244743cdba45686cfb680486))


### Bug Fixes

* **templates:** translate the imprint link ([5ded88c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/5ded88ccba9cda48132d8d717b9fda5d2325a12c))

## [1.3.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.2.2...v1.3.0) (2024-10-17)


### Features

* **settings:** reuse PUBLIC_URL for APIS_BASE_URI ([f71b5b7](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/f71b5b7560050132c501eafad1228845c77db343)), closes [#107](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/107)

## [1.2.2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.2.1...v1.2.2) (2024-10-14)


### Bug Fixes

* **template:** make imprint url handling more robust ([1009f15](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1009f15e451470e25faf810410cf90c91bfe4f7c))

## [1.2.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.2.0...v1.2.1) (2024-10-01)


### Bug Fixes

* **settings:** drop csvexport from INSTALLED_APPS ([9963ca8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/9963ca8c24e44ebba79e5bc17e42e723480ca879)), closes [#100](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/100)

## [1.2.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.1.2...v1.2.0) (2024-09-30)


### Features

* add imprint functionality ([6384f3c](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6384f3ccf84b24a0dbb8fecbb8ee5541e1c7aad4))
* **settings:** set GIT_REPOSITORY_URL variable ([179b360](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/179b360f29a2aa1c8f9e3c349c371ef99d372109))

## [1.1.2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.1.1...v1.1.2) (2024-09-26)


### Bug Fixes

* **settings:** move apis_relations before apis_entities ([ca045fd](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ca045fd40c9601da1ef5c80577300f278a5d171f))

## [1.1.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.1.0...v1.1.1) (2024-09-05)


### Bug Fixes

* **INSTALLED_APPS:** move apis_core.core further down in the app list ([7f4ded7](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7f4ded7a25fb90c938bfa44e8dd1ae7ded7cfe0b))
* **INSTALLED_APPS:** move apis_ontology before apis_core in app list ([6ae85d3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6ae85d37ba2320c39cffa4fa5d473f6301ba3b21)), closes [#29](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/29)

## [1.1.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v1.0.0...v1.1.0) (2024-08-19)


### Features

* **settings:** introduce logging configuration ([1a534c6](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1a534c64678377880c93d1f353e5c5c7320c9346))


### Bug Fixes

* **middlware:** add middleware to prevent clickjacking ([3105cea](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/3105cea46ee65b3af7dc2b0c436c80f46ae9d70e)), closes [#47](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/47)
* **settings:** drop unused settings ([19aff16](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/19aff16df8ce186ab7177d0e542cc673b4941fe9)), closes [#46](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/46)
* **spectacular:** set DEFAULT_GENERATOR_CLASS ([41d3c49](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/41d3c49d0985aa2bb7ea6fa7f83c4b0fa2a7514e)), closes [#84](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/84)

## [1.0.0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.24...v1.0.0) (2024-04-08)


### ⚠ BREAKING CHANGES

* drop reversion

### Bug Fixes

* drop reversion ([d92cbe0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d92cbe02e659231264d478907fb2cf18fcbcd612))

## [0.1.24](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.23...v0.1.24) (2024-01-26)


### Bug Fixes

* add ldap support ([4dfb76e](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/4dfb76e90c2a9a7ff1e834bf0645d55e15692c68))

## [0.1.23](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.22...v0.1.23) (2024-01-19)


### Bug Fixes

* add 'generic' app to INSTALLED_APPS ([6e2d382](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6e2d3820ce7fc2051184c78e9065213e53e27fab))

## [0.1.22](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.21...v0.1.22) (2023-12-20)


### Bug Fixes

* set drf DEFAULT_PERMISSION_CLASSES to model permission ([91c4457](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/91c4457dbd0e4c54cd09b5c2c2510db5adb508ff))
* TEMPLATES: remove apis_ontology/templates from DIRS ([e7945e0](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/e7945e07bdf2865d1708ca0fedc627b18be7bb18))
* use random secret key instead of hardcoding it ([0f7e9e3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/0f7e9e3d760104596c1f3b1bca950817c8ef1cce)), closes [#65](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/65)

## [0.1.21](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.20...v0.1.21) (2023-12-19)


### Bug Fixes

* typo in ROOT_URLCONF ([9840a10](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/9840a10c6c7097ec9c18f51d8a34f8e0d5515aa8))

## [0.1.20](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.19...v0.1.20) (2023-12-19)


### Bug Fixes

* bump default template pack for crispy ([9d8a3cb](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/9d8a3cb6450640e8b8a9a97bc634bbbc7ff94249))

## [0.1.19](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.18...v0.1.19) (2023-12-19)


### Bug Fixes

* add crispy_bootstrap4 to list of installed apps ([11f7300](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/11f7300294f3e4d9c2621318a1154fd70901a701))
* drop apis_labels from installed apps ([5c9a086](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/5c9a0864e5c3daac1d143b61312e057fc20c00f6))

## [0.1.18](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.17...v0.1.18) (2023-12-13)


### Bug Fixes

* drop deprecated context_processors ([ca114f3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ca114f3b08163d77b23ed146d82712248930c3f9)), closes [#55](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/55)

## [0.1.17](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.16...v0.1.17) (2023-12-11)


### Bug Fixes

* drop django-cors-headers related settings ([6620c56](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/6620c5612b238d8ee024b45101e852cdf8defdfe))

## [0.1.16](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.15...v0.1.16) (2023-11-30)


### Bug Fixes

* drop deprecated context_processors ([7aa4ce6](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7aa4ce64ffd211552f21688324a4abedc74e485c))
* set ROOT_URLCONF to correct module ([2afd483](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/2afd483fb4dbafb26626ade3149c3ed6e86b9bb2))

## [0.1.15](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.14...v0.1.15) (2023-11-29)


### Bug Fixes

* get `ALLOWED_HOSTS` from `PUBLIC_URL` ([443b0c2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/443b0c267e57b505832a0be8c962dba148792372)), closes [#28](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/28)

## [0.1.14](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.13...v0.1.14) (2023-11-29)


### Bug Fixes

* add initial README ([ad64d78](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/ad64d780830379cc4fbfee40f5f2096cab18b7a2))

## [0.1.13](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.12...v0.1.13) (2023-11-29)


### Bug Fixes

* provide default database setup ([911c0ec](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/911c0ec32908540aad65b85f9db2427556ff1da1)), closes [#33](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/33)

## [0.1.12](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.11...v0.1.12) (2023-11-28)


### Bug Fixes

* drop apis-override-select2js from dependencies ([0f7840f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/0f7840f6b7657f3cc2b2f7df32a1d9992a233892))

## [0.1.11](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.10...v0.1.11) (2023-11-24)


### Bug Fixes

* disable sentry tracing ([aa7c401](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/aa7c4019ca72938ad51254c2ff723696c03d4eef))

## [0.1.10](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.9...v0.1.10) (2023-10-19)


### Bug Fixes

* include ALLOWED_CIDR_NETS into settings ([dcbcfb8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/dcbcfb8bd1c5c3254fc0c3a936e6e1bf11a968cb)), closes [#19](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/19)

## [0.1.9](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.8...v0.1.9) (2023-10-18)


### Bug Fixes

* drop charts dependency ([d9ccb0f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d9ccb0f7d064dbbb92b36c7abea4761e42036c3b))
* drop WSGI_APPLICATION ([28aff2a](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/28aff2aa5e21b4b332bbfb7c95c4d54676724edf)), closes [#24](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/24)

## [0.1.8](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.7...v0.1.8) (2023-10-05)


### Bug Fixes

* add apis_core.core to installed apps ([7d65db9](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/7d65db9a5a09c5607d79a3bfcab69c977c054fbf))

## [0.1.7](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.6...v0.1.7) (2023-09-13)


### Bug Fixes

* remove the list view template override ([234ab87](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/234ab877f09a92e2e2bb9c2537e14ab30ee0d5f7))

## [0.1.6](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.5...v0.1.6) (2023-09-01)


### Bug Fixes

* drop ACDH_IMPRINT_URL ([1f43725](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/1f437257aa32496ce9af81311339dab5f5b15441))

## [0.1.5](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.4...v0.1.5) (2023-08-23)


### Bug Fixes

* drop override of default templates ([f9fea45](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/f9fea45713bd9fe8f687c0afc8c6d3b88775cb8e))

## [0.1.4](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.3...v0.1.4) (2023-08-23)


### Bug Fixes

* drop webpage ([71dc49d](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/71dc49d7ff3b02bfb642967ea5fa042d945fd439))

## [0.1.3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.2...v0.1.3) (2023-08-21)


### Bug Fixes

* drop guardian settings ([167531e](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/167531e619d1ec0f429e35f342cba272404c377c))

## [0.1.2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.1...v0.1.2) (2023-08-18)


### Bug Fixes

* **deps:** add whitenoise dependency ([d5c43ce](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d5c43ceed7ab71cc725b56e4d5f6c05886121d6f)), closes [#3](https://github.com/acdh-oeaw/apis-acdhch-default-settings/issues/3)
* **deps:** loosen Python dependency version constraints ([56cf49f](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/56cf49f0fc53b74ebbf6d1057c3876184f3b96b6))

## [0.1.1](https://github.com/acdh-oeaw/apis-acdhch-default-settings/compare/v0.1.0...v0.1.1) (2023-08-16)


### Bug Fixes

* **deps:** add apis-override-select2js to the dependencies ([422f8e2](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/422f8e2e948cbeee7bdb4f64a0735f9204eb5136))

## 0.1.0 (2023-08-16)


### Bug Fixes

* rename module folder to adhere to Python convention ([d9d873b](https://github.com/acdh-oeaw/apis-acdhch-default-settings/commit/d9d873b1b5decf53dcaa58cf4a0a95f6a2b3f944))
