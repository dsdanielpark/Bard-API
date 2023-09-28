var e8a = {
            DEFAULT: "default",
            Bxa: "flights",
            Yxa: "hotels",
            hya: "images_advanced",
            iya: "images_basic",
            jya: "images_in_tables",
            kya: "image_generation",
            lya: "implicit_code_execution",
            hza: "maps_basic",
            hAa: "processing_state",
            vAa: "safety_disclaimer",
            NAa: "shopping_multiple_products",
            PAa: "shopping_single_product",
            kBa: "title_generation",
            mBa: "tool_consent_external",
            nBa: "tool_consent_workspace",
            oBa: "tool_consent_workspace_eecc",
            pBa: "tool_disclaimer",
            qBa: "tool_sources_many",
            rBa: "tool_sources_none_workspace_response",
            sBa: "tool_sources_some",
            fCa: "youtube_channel",
            gCa: "youtube_playlist",
            hCa: "youtube_single_video"
        }
          , nS = function() {
            this.ha = this.ma = 0;
            this.Kf = "default";
            var a = {
                conversationId: "c_10",
                title: "Math test",
                timestamp: new Date("2023-04-01"),
                pinned: !0,
                hidden: !1
            }
              , b = {
                conversationId: "c_11",
                title: "Show me pictures of Barcelona",
                timestamp: new Date("2023-04-02"),
                pinned: !0,
                hidden: !1
            }
              , c = {
                conversationId: "c_12",
                title: "Why is the sky blue",
                timestamp: new Date("2023-04-03"),
                pinned: !0,
                hidden: !1
            }
              , d = {
                conversationId: "c_13",
                title: "Another Math test",
                timestamp: new Date("2023-04-04"),
                pinned: !0,
                hidden: !1
            }
              , e = {
                conversationId: "c_14",
                title: "Show me pictures of Paris",
                timestamp: new Date("2023-04-05"),
                pinned: !0,
                hidden: !1
            }
              , f = new Date("2023-04-06");
            var g = new ir;
            var h = new BD;
            h = _.kp(h, 1, 2);
            g = _.vo(g, BD, 1, h);
            this.ka = [a, b, c, d, e, {
                conversationId: "c_15",
                title: "Why is the sky red",
                timestamp: f,
                pinned: !0,
                hidden: !1,
                Sz: _.Cc(g)
            }, {
                conversationId: "c_16",
                title: "Show me flights departing from ZRH tomorrow",
                timestamp: new Date("2023-04-07"),
                pinned: !0,
                hidden: !1
            }, {
                conversationId: "c_17",
                title: "How old are you?",
                timestamp: new Date("2023-04-08"),
                pinned: !0,
                hidden: !1
            }, {
                conversationId: "c_20",
                title: "Show me a cat",
                timestamp: new Date("2023-04-04"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_21",
                title: "Help me incorporate more high-protein vegan options in my diet",
                timestamp: new Date("2023-04-05"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_22",
                title: "Tell me about the code within the google/jax GitHub repo",
                timestamp: new Date("2023-04-06"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_23",
                title: 'Debug this error message: "FileNotFoundError: [Errno 2]',
                timestamp: new Date("2023-04-07"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_24",
                title: "Help me understand if lightning can strike the same place twice",
                timestamp: new Date("2023-04-08"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_25",
                title: "Tell me about the code within the google/jax GitHub repo 2",
                timestamp: new Date("2023-04-09"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_26",
                title: 'Debug this error message: "FileNotFoundError: [Errno 2] 2',
                timestamp: new Date("2023-04-10"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_27",
                title: "What is the weather like?",
                timestamp: new Date("2023-04-11"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_28",
                title: "How old is Obama?",
                timestamp: new Date("2023-04-12"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_29",
                title: "This is a test",
                timestamp: new Date("2023-04-13"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_30",
                title: "Hey! How are you doing?",
                timestamp: new Date("2023-04-14"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_31",
                title: "What time is it?",
                timestamp: new Date("2023-04-15"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_32",
                title: "Write me some hello worlds in Python?",
                timestamp: new Date("2023-04-16"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_33",
                title: "Explain Fermat's last theorem in details",
                timestamp: new Date("2023-04-17"),
                pinned: !1,
                hidden: !1
            }, {
                conversationId: "c_34",
                title: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ex purus,\nfinibus  eget euismod at, posuere in enim. Aenean consequat augue lorem,\net tempor arcu pellentesque non. Quisque dui lectus, pulvinar in tellus\nin, pharetra imperdiet ante. Aliquam interdum, neque sit amet gravida\nbibendum, quam metus maximus ligula, non lacinia mauris neque vitae ex.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget\nbibendum erat. Maecenas condimentum, dui ullamcorper aliquam maximus,\nsem velit tempor ex, ut tincidunt lectus justo nec tortor. Suspendisse\njusto ligula, mattis bibendum hendrerit ut, consectetur vel erat.\nDonec et nisl sit amet dui tincidunt dignissim.",
                timestamp: new Date("2023-04-18"),
                pinned: !1,
                hidden: !1
            }]
        }
          , f8a = function(a) {
            return Object.values(e8a).filter(function(b) {
                return a.includes(b)
            }).sort(function(b, c) {
                return c.length - b.length
            })[0]
        };
        nS.prototype.JK = function(a) {
            var b = this.ma
              , c = a.textQuery;
            this.ma++;
            var d;
            switch (null != (d = f8a(c)) ? d : this.Kf) {
            case "flights":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some flights that might work for you:\n\nhttp://googleusercontent.com/flight_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [],
                            CK: [{
                                hb: "http://googleusercontent.com/flight_content/1",
                                mb: 0,
                                title: "Flights label for XXX",
                                Zl: {
                                    displayName: "Google Flights",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/travel_flights/v7/192px.svg"
                                },
                                Aba: 2,
                                trips: [{
                                    Sm: {
                                        uD: "United",
                                        tD: "https://www.gstatic.com/flights/airline_logos/70px/UA.png",
                                        RF: "JFK",
                                        iE: "SFO",
                                        departureTime: "8:34 AM",
                                        arrivalTime: "10:45 AM",
                                        duration: "2 hr 11 min",
                                        JG: "Nonstop"
                                    },
                                    Wk: "$324"
                                }, {
                                    Sm: {
                                        uD: "Lufthansa",
                                        tD: "https://www.gstatic.com/flights/airline_logos/70px/LH.png",
                                        RF: "LHR",
                                        iE: "MUC",
                                        departureTime: "8:34 AM",
                                        arrivalTime: "10:45 AM",
                                        duration: "2 hr 11 min",
                                        JG: "1 stop"
                                    },
                                    Wk: "$570"
                                }, {
                                    Sm: {
                                        uD: "Turkish Airlines",
                                        tD: "https://www.gstatic.com/flights/airline_logos/70px/TK.png",
                                        RF: "IST",
                                        iE: "HND",
                                        departureTime: "8:34 AM",
                                        arrivalTime: "10:45 AM",
                                        duration: "2 hr 11 min",
                                        JG: "2 stops"
                                    },
                                    Wk: "$890"
                                }, {
                                    Sm: {
                                        uD: "Southwest",
                                        tD: "https://www.gstatic.com/flights/airline_logos/70px/WN.png",
                                        RF: "LGA",
                                        iE: "DAL",
                                        departureTime: "8:34 AM",
                                        arrivalTime: "10:45 AM",
                                        duration: "2 hr 11 min",
                                        JG: "Nonstop"
                                    },
                                    Wk: "unavailable"
                                }],
                                aX: "https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDIzLTA5LTEzag0IAxIJL20vMDJfMjg2cgwIAxIIL20vMDZ0MnRAAUgBcAGCAQsI____________AZgBAg&gl=US"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "hotels":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some hotels in Madison:\n\nhttp://googleusercontent.com/property_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [],
                            Zz: [{
                                hb: "http://googleusercontent.com/property_content/1",
                                mb: 0,
                                title: "Hotels label for XXX",
                                Zl: {
                                    displayName: "Google Hotels",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/travel_hotels/v7/192px.svg"
                                },
                                V6: [{
                                    displayName: "Hotel Indigo Madison Downtown, an IHG Hotel",
                                    jr: ["//lh3.googleusercontent.com/p/AF1QipM-woOZ5FqkRgDCjKOxgXzXxX9Q1xURZDhGxTvN=w592-h404-n-k-rw-no-v1", "//lh5.googleusercontent.com/p/AF1QipOvMxwOSWNMP0m5h46AyFPiDjM0ks3ZvbOdJVlp=s204-w204-h116-p-n-k-no", "//lh5.googleusercontent.com/p/AF1QipP9lI4UkQaqhnIJQQjpDQ3PBdH1Be2bcQYFmxNJ=s204-w204-h116-p-n-k-no"],
                                    kk: 4.8,
                                    Ul: 514,
                                    ir: "3-star hotel",
                                    description: "Set along Highway 151, this relaxed hotel is less than a mile from the Wisconsin State Capitol, and 2 miles from the Madison Museum of Contemporary Art.",
                                    Lw: "$100",
                                    mz: "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4429192%2C4570331%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4924070%2C4965990%2C4990494%2C72262033%2C72262036%2C72285074%2C72286089%2C72298667%2C72300991%2C72301739%2C72302247%2C72305577%2C72313834%2C72314854%2C72317059%2C72318437%2C72322083&hl=en-US&gl=us&cs=1&ssta=1&ts=CAESCAoCCAMKAggDGhwSGhIUCgcI5w8QCBgEEgcI5w8QCBgFGAEyAhAAKgcKBToDVVNE&qs=CAE4BkILCVjrvUaPRq2fGAFCCwm1VnmhbrPh6hgBQgsJoG0WEiT3RCwYAQ&ap=MABoAQ&ictx=1&sa=X&ved=0CAAQ5JsGahcKEwio0L2e48OAAxUAAAAAHQAAAAAQDA"
                                }, {
                                    displayName: "Hilton Garden Inn Madison Downtown",
                                    jr: ["//lh3.googleusercontent.com/p/AF1QipMzh6s-AiMsFFkYz1CYkzAy9TVunTT7E-7elEH7=w592-h404-n-k-rw-no-v1", "//lh3.googleusercontent.com/p/AF1QipPOgQGMAp8sqN3LFr1P62FnywE2BmM0R7K2VWsH=w592-h404-n-k-rw-no-v1", "//lh3.googleusercontent.com/p/AF1QipNL-T9b8AQCoNfMFXLK1q9visJGj6p7r7u5SknA=w592-h404-n-k-rw-no-v1"],
                                    kk: 4.7,
                                    Ul: 242,
                                    ir: "3-star hotel",
                                    description: "Set Downtown, this relaxed hotel is 6 minutes' walk from University of Wisconsin-Madison, a mile from the Wisconsin State Capitol and 8 miles from Interstate 90.",
                                    Lw: "$322",
                                    mz: "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4429192%2C4570331%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4924070%2C4965990%2C4990494%2C72262033%2C72262036%2C72285074%2C72286089%2C72298667%2C72300991%2C72301739%2C72302247%2C72305577%2C72311299%2C72313834%2C72314854%2C72317059%2C72318437%2C72322083&hl=en-US&gl=us&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAaKQoLEgk6B01hZGlzb24SGhIUCgcI5w8QCBgEEgcI5w8QCBgFGAEyAhAAKgcKBToDVVNE&qs=CAEyuwFDZ3NJc3FTRnpzNlFfZmEyQVJBQkdudEJVR1JtWWxjMFQxVjZXR2hVTVdoSlRIWlhkSEE1UkdaemVrWTRSa1YzUVdvME1XNWZSbHBYY0U5bE5sTnRTVmhOU1hoVU0zWjNiVXBPWlZKRmJsUjBNRVpIVXkxTlZHTllTblF3UXpKUWFuZHZVR2x5UlV4bGFWRkRibU5vZVY5ckxUaHpRVFZGVG0xQ1VrZHlaVE5zV1hacWRucHFkakp1VmpROAZCCwlY671Gj0atnxgBQgsJtVZ5oW6z4eoYAUILCcifSiOTAsnlGAE&ap=KigKEgk0kAcve21FQBG8QElh52JWwBISCUVG8H8MpUVAEbxASaEjUFbAMABoAQ&ictx=1&sa=X&ved=0CAAQ5JsGahgKEwiY48yh5sOAAxUAAAAAHQAAAAAQ-gc"
                                }, {
                                    displayName: "Clarion Suites at the Alliant Energy Center",
                                    jr: ["//lh3.googleusercontent.com/p/AF1QipNDCWHAbw125QLigEbE_E6xbtFKFg6VmfJsnVxn=w592-h404-n-k-rw-no-v1", "//lh3.googleusercontent.com/p/AF1QipMfMDqrqofu-UaTrg-In_hwPqJrKdSn3w-swDrb=w592-h404-n-k-rw-no-v1", "//lh3.googleusercontent.com/p/AF1QipM5KbWxMxzs5o55U-f8EF-MaOrNdTtw1rsqOc17=w592-h404-n-k-rw-no-v1"],
                                    kk: 4.2,
                                    Ul: 687,
                                    ir: "3-star hotel",
                                    description: "Part of the Alliant Energy Center event complex, this informal, all-suite hotel is 2.7 miles from University of Wisconsin-Madison and 7.5 miles from Dane County Regional Airport.",
                                    Lw: "$339",
                                    mz: "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4429192%2C4570331%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4924070%2C4965990%2C4990494%2C72262033%2C72262036%2C72285074%2C72286089%2C72298667%2C72300991%2C72301739%2C72302247%2C72305577%2C72311299%2C72313834%2C72314854%2C72317059%2C72318437%2C72322083&hl=en-US&gl=us&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAaKQoLEgk6B01hZGlzb24SGhIUCgcI5w8QCBgEEgcI5w8QCBgFGAEyAhAAKgcKBToDVVNE&qs=CAEyugFDZ29JZ29yRzlhV0R5T3hJRUFFYWUwRlFaR1ppVnpWNmVXWlhNVTQ0T0ZoeE5taHlaVk5hVkZZM2RUY3dOVE5RYXpkRmNsUTJWRTVoYWt3MWQzRjJjQzFwY25scU9YZHdXVTlqYUhkRU1tWkxRalYyTjFkdGNqQjFWbWRrVXpWUk9VSlBaMWhWZUhaeWVtbG1jbWhwVG5CVFgxb3hOVTFYZUdzMlpuZHpTVVZXVVhGVlRuQTNOMjVrV1E4BkILCVjrvUaPRq2fGAFCCwm1VnmhbrPh6hgBQgsJyJ9KI5MCyeUYAQ&ap=KigKEgk0kAcve21FQBG8QElh52JWwBISCUVG8H8MpUVAEbxASaEjUFbAMABoAQ&ictx=1&sa=X&ved=0CAAQ5JsGahgKEwiY48yh5sOAAxUAAAAAHQAAAAAQkQk"
                                }, {
                                    displayName: "The Empty Hotel",
                                    jr: [],
                                    kk: 1,
                                    Ul: 5,
                                    ir: "3-star hotel",
                                    description: "",
                                    Lw: "",
                                    mz: "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4429192%2C4570331%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4924070%2C4965990%2C4990494%2C72262033%2C72262036%2C72285074%2C72286089%2C72298667%2C72300991%2C72301739%2C72302247%2C72305577%2C72311299%2C72313834%2C72314854%2C72317059%2C72318437%2C72322083&hl=en-US&gl=us&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAaKQoLEgk6B01hZGlzb24SGhIUCgcI5w8QCBgEEgcI5w8QCBgFGAEyAhAAKgcKBToDVVNE&qs=CAEyugFDZ29JZ29yRzlhV0R5T3hJRUFFYWUwRlFaR1ppVnpWNmVXWlhNVTQ0T0ZoeE5taHlaVk5hVkZZM2RUY3dOVE5RYXpkRmNsUTJWRTVoYWt3MWQzRjJjQzFwY25scU9YZHdXVTlqYUhkRU1tWkxRalYyTjFkdGNqQjFWbWRrVXpWUk9VSlBaMWhWZUhaeWVtbG1jbWhwVG5CVFgxb3hOVTFYZUdzMlpuZHpTVVZXVVhGVlRuQTNOMjVrV1E4BkILCVjrvUaPRq2fGAFCCwm1VnmhbrPh6hgBQgsJyJ9KI5MCyeUYAQ&ap=KigKEgk0kAcve21FQBG8QElh52JWwBISCUVG8H8MpUVAEbxASaEjUFbAMABoAQ&ictx=1&sa=X&ved=0CAAQ5JsGahgKEwiY48yh5sOAAxUAAAAAHQAAAAAQkQk"
                                }, {
                                    displayName: "The Hotel Without Price",
                                    jr: ["//lh3.googleusercontent.com/p/AF1QipNPCWtrpiW8yvz0YyPZ9ERrrs1XAlWpfEpaPRzK=w287-h192-n-k-rw-no-v1"],
                                    kk: 5,
                                    Ul: 256,
                                    ir: "5-star hotel",
                                    description: "Exclusive Hotel. Call for price.",
                                    Lw: "",
                                    mz: "https://www.google.com/travel/search?q=google%20hotels&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4429192%2C4570331%2C4597339%2C4757164%2C4814050%2C4850738%2C4864715%2C4874190%2C4886480%2C4893075%2C4924070%2C4965990%2C4990494%2C72262033%2C72262036%2C72285074%2C72286089%2C72298667%2C72300991%2C72301739%2C72302247%2C72305577%2C72311299%2C72313834%2C72314854%2C72317059%2C72318437%2C72322083&hl=en-US&gl=us&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAaKQoLEgk6B01hZGlzb24SGhIUCgcI5w8QCBgEEgcI5w8QCBgFGAEyAhAAKgcKBToDVVNE&qs=CAEyugFDZ29JZ29yRzlhV0R5T3hJRUFFYWUwRlFaR1ppVnpWNmVXWlhNVTQ0T0ZoeE5taHlaVk5hVkZZM2RUY3dOVE5RYXpkRmNsUTJWRTVoYWt3MWQzRjJjQzFwY25scU9YZHdXVTlqYUhkRU1tWkxRalYyTjFkdGNqQjFWbWRrVXpWUk9VSlBaMWhWZUhaeWVtbG1jbWhwVG5CVFgxb3hOVTFYZUdzMlpuZHpTVVZXVVhGVlRuQTNOMjVrV1E4BkILCVjrvUaPRq2fGAFCCwm1VnmhbrPh6hgBQgsJyJ9KI5MCyeUYAQ&ap=KigKEgk0kAcve21FQBG8QElh52JWwBISCUVG8H8MpUVAEbxASaEjUFbAMABoAQ&ictx=1&sa=X&ved=0CAAQ5JsGahgKEwiY48yh5sOAAxUAAAAAHQAAAAAQkQk"
                                }]
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "image_generation":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Draft for image generation with IMAGES ONLY from 0P image generator - Miro.\n\n[Generated Image of the universe]",
                        Kb: {
                            ad: !0,
                            hc: [],
                            Ml: {
                                Nk: [{
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-1633.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-1633.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 3,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2006.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2006.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 3,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2305.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2305.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 3,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 3,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0,
                                    errorMessage: "Couldn't load."
                                }],
                                Kf: 1
                            }
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Draft for image generation WITH TEXT from 0P image generator - Miro.\n\nIn the beginning, there was nothing. No space, no time, no matter. Just a vast, empty void.\n\nThen, something happened. A tiny point of energy appeared in the void. This point of energy was incredibly hot and dense, and it began to expand. As it expanded, it cooled, and matter began to form.\n\n[Generated Image of the big bang]\n\nOver time, the matter in the universe clumped together to form stars, galaxies, and planets. Our own solar system formed about 4.5 billion years ago, and our planet, Earth, was born about 3.5 billion years ago.\n\n[Generated Image of the universe]\n",
                        Kb: {
                            ad: !0,
                            hc: [],
                            Ml: {
                                Nk: [{
                                    wb: "https://img.freepik.com/premium-photo/big-bang-starry-galaxy-generative-ai_835692-70.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/big-bang-starry-galaxy-generative-ai_835692-70.jpg",
                                    Wi: !0,
                                    Og: {
                                        li: 2,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the big bang]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    Wi: !0,
                                    Og: {
                                        li: 2,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }],
                                Kf: 2
                            }
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-3",
                        index: 2,
                        textResponse: "Draft for image generation with IMAGES ONLY from 3P image generator - Adobe Firefly.\n\n[Generated Image of the universe]",
                        Kb: {
                            ad: !0,
                            hc: [],
                            Ml: {
                                Nk: [{
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-1633.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-1633.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2006.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2006.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2305.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-neon-nebula-space-art-galaxy-creative-background-ai_564714-2305.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    Wi: !1,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0,
                                    errorMessage: "Couldn't load."
                                }],
                                Kf: 1
                            }
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-4",
                        index: 3,
                        textResponse: "Draft for image generation WITH TEXT from 3P image generator - Adobe Firefly.\n\nIn the beginning, there was nothing. No space, no time, no matter. Just a vast, empty void.\n\nThen, something happened. A tiny point of energy appeared in the void. This point of energy was incredibly hot and dense, and it began to expand. As it expanded, it cooled, and matter began to form.\n\n[Generated Image of the big bang]\n\nOver time, the matter in the universe clumped together to form stars, galaxies, and planets. Our own solar system formed about 4.5 billion years ago, and our planet, Earth, was born about 3.5 billion years ago.\n\n[Generated Image of the universe]\n",
                        Kb: {
                            ad: !0,
                            hc: [],
                            Ml: {
                                Nk: [{
                                    wb: "https://img.freepik.com/premium-photo/big-bang-starry-galaxy-generative-ai_835692-70.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/big-bang-starry-galaxy-generative-ai_835692-70.jpg",
                                    Wi: !0,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the big bang]",
                                    mb: 0
                                }, {
                                    wb: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    imageUrl: "https://img.freepik.com/premium-photo/starfield-with-nebulagenerative-ai_76964-18204.jpg",
                                    Wi: !0,
                                    Og: {
                                        li: 1,
                                        prompt: "A universe with stars and a nebulous cloud."
                                    },
                                    hb: "[Generated Image of the universe]",
                                    mb: 0
                                }],
                                Kf: 2
                            }
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_DEVICE",
                        og: !0,
                        Cx: ""
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "images_basic":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Sure, here is a description of Barcelona with images:\n\n**Barcelona is a city of contrasts.** It is a city of old and new, of sea and mountains, of art and architecture.\n\n**In the Gothic Quarter, you can wander through narrow streets and alleyways lined with medieval buildings.** The Pla\u00e7a de Sant Jaume is the heart of the Gothic Quarter, and it is here that you can find the Barcelona City Hall and the Palau de la Generalitat de Catalunya, the seat of the Catalan government.\n\n[Image of the Gothic Quarter][Image of the Pla\u00e7a de Sant Jaume]\n\n**Las Ramblas is a wide boulevard that runs through the heart of Barcelona.** It is lined with shops, restaurants, and street performers. The Ramblas is a great place to people-watch and soak up the atmosphere of the city.\n\n[Image of Las Ramblas]  [Image of a street performer on Las Ramblas]\n\n**The Barceloneta Beach is a popular spot for swimming, sunbathing, and people-watching.** It is a long stretch of sandy beach that is perfect for relaxing in the sun or taking a dip in the Mediterranean Sea.\n\n[Image of the Barceloneta Beach]\n\n[Image of people sunbathing on the Barceloneta Beach]\n\n**Barcelona is also a city of art and architecture.** Antoni Gaud\u00ed, one of the most famous architects of all time, left his mark on the city with his unique and whimsical buildings. The Sagrada Familia, Park G\u00fcell, and Casa Mil\u00e0 are just a few of Gaud\u00ed's masterpieces.\n\n[Image of the Sagrada Familia]\n\n[Image of Park G\u00fcell]\n\n[Image of Casa Mil\u00e0]\n\n**Barcelona is a city that has something to offer everyone.** Whether you are interested in history, art, architecture, or simply want to relax on the beach, Barcelona is the perfect place to visit.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://assets2.devourtours.com/wp-content/uploads/Gothic-Quarter-in-Barcelona-1.png",
                                title: "Gothic Quarter",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of the Gothic Quarter]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/518023780/photo/city-council-on-barcelona-spain-plaza-de-sant-jaume.jpg?s=1024x1024&w=is&k=20&c=_HJscUruQIxBV-_HkfJb6BfNkUfPr1to2R2FtuooAOI=",
                                title: "Pla\u00e7a de Sant Jaume",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of the Pla\u00e7a de Sant Jaume]",
                                mb: 0
                            }, {
                                wb: "https://c8.alamy.com/comp/MTTM1R/las-ramblas-barcelona-stalls-along-the-busy-rambla-sant-josep-barcelona-catalunya-spain-MTTM1R.jpg",
                                title: "Image of Las Ramblas",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of Las Ramblas]",
                                mb: 0
                            }, {
                                wb: "https://img.theculturetrip.com/wp-content/uploads/2018/04/5095625939_2fce24c708_b.jpg",
                                title: "A street performer on Las Ramblas",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of a street performer on Las Ramblas]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/951974648/photo/barceloneta-beach-in-barcelona-with-colorful-sky-at-sunrise-seafront-beach-coast-in-spain.jpg?s=612x612&w=0&k=20&c=h7AZ-chjljk4TnJOf75x8xKqlwtDULBk_Cwf9pOzidQ=",
                                title: "Barceloneta Beach",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of the Barceloneta Beach]",
                                mb: 0
                            }, {
                                wb: "https://thumbs.dreamstime.com/b/people-sunbathing-mediterranean-beach-barcelona-spain-june-june-barcelona-spain-barceloneta-one-most-popular-48692023.jpg",
                                title: "People sunbathing on the Barceloneta Beach",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of people sunbathing on the Barceloneta Beach]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/1130443789/photo/sagrada-familia-basilica-in-barcelona.jpg?b=1&s=170667a&w=0&k=20&c=Ufz9DWJ-ylTv1YeBrsy48jKZJ6EUm2dOEg38aT8j5X0=",
                                title: "Sagrada Familia",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of the Sagrada Familia]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/534846887/photo/park-guell-in-barcelona-spain.jpg?s=612x612&w=0&k=20&c=57iKMZfKaK16TGoWQzlFs6uiGpB3APPiu1TLEbI3OCQ=",
                                title: "Park G\u00fcell",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of Park G\u00fcell]",
                                mb: 0
                            }, {
                                wb: "https://upload.wikimedia.org/wikipedia/commons/d/de/Casa_Mil%C3%A0%2C_general_view.jpg",
                                title: "Casa Mil\u00e0",
                                sourceUrl: "https://google.com",
                                yc: "Google",
                                zi: "https://www.google.com/s2/favicons?sz=16&domain_url=google.com",
                                hb: "[Image of Casa Mil\u00e0]",
                                mb: 0
                            }]
                        },
                        Cd: {
                            Ce: pr([[{
                                start: 100,
                                end: 140
                            }], [{
                                start: 400,
                                end: 460
                            }], [{
                                start: 600,
                                end: 666
                            }]]),
                            hg: {
                                status: 0
                            },
                            mode: 0
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Short paragraph about something\n\n[Image of a flower]\n\nFlowers are the reproductive organs of flowering plants. They are typically brightly colored and fragrant, and they attract pollinators such as bees, butterflies, and hummingbirds. Flowers come in a wide variety of shapes, sizes, and colors. Some flowers are edible, while others are used for their medicinal properties. Flowers are also used for decorative purposes, and they are often used in bouquets, arrangements, and landscaping.\n\n[Image of a flower]\n\nThe end.\n\n[Image of a flower]",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://hips.hearstapps.com/hmg-prod/images/close-up-of-purple-crocus-flowers-united-kingdom-uk-royalty-free-image-1674159456.jpg",
                                sourceUrl: "https://google.com",
                                yc: "Some very long source text",
                                hb: "[Image of a flower]",
                                mb: 0,
                                title: "flower"
                            }]
                        },
                        Cd: {
                            Ce: pr([[{
                                start: 10,
                                end: 20
                            }], [{
                                start: 21,
                                end: 62
                            }]]),
                            hg: {
                                status: 0
                            },
                            mode: 0
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-3",
                        index: 2,
                        textResponse: "Sure, here are some images of cats, along with a description of each kind:\n\n* **Persian cats** are known for their long, thick fur and round faces. They are a popular breed of cat, and are often described as being gentle and affectionate.\n[Image of a Persian cat]\n\n* **Abyssinian cats** are known for their sleek, athletic bodies and distinctive ticking fur. They are a playful and intelligent breed of cat, and are often described as being curious and inquisitive.\n[Image of an Abyssinian cat]\n\n* **Siamese cats** are known for their distinctive markings, which consist of dark points on the face, ears, legs, and tail. They are a vocal and affectionate breed of cat, and are often described as being loyal and devoted.\n[Image of a Siamese cat]\n\n* **Maine Coon cats** are the largest breed of domestic cat. They are known for their long, thick fur, bushy tails, and tufted ears. They are a gentle and affectionate breed of cat, and are often described as being laid-back and easygoing.\n[Image of a Maine Coon cat]\n\n* **Scottish Fold cats** are known for their folded ears, which give them a distinctive appearance. They are a gentle and affectionate breed of cat, and are often described as being playful and curious.\n[Image of a Scottish Fold cat]\n\nThese are just a few of the many different breeds of cats that exist. Each breed has its own unique set of characteristics, making them all special in their own way.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://www.thesprucepets.com/thmb/5OSN_p9hUfPssKsJORQDGnAz_tQ=/1963x0/filters:no_upscale():strip_icc()/GettyImages-181861505-4e63227ed0a14dc9bfe86848ef54caf3.jpg",
                                sourceUrl: "https://google.com",
                                yc: "a Persian cat",
                                hb: "[Image of a Persian cat]",
                                mb: 0
                            }, {
                                wb: "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRArbVS6wpy-yY7IGo8T1zWrr0wl3mpQOhoqpMEtygh_XyWqO7m_3gyyJsfrFF1lP6hLcv_Uf7HjOAdD7M",
                                sourceUrl: "https://google.com",
                                yc: "an Abyssinian cat",
                                hb: "[Image of an Abyssinian cat]",
                                mb: 0
                            }, {
                                wb: "https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-06/Siamese-Cat_0.jpg?itok=Qy1J6ZDS",
                                sourceUrl: "https://google.com",
                                yc: "a Siamese cat",
                                hb: "[Image of a Siamese cat]",
                                mb: 0
                            }, {
                                wb: "https://static.boredpanda.com/blog/wp-content/uploads/2015/11/maine-coon-cats-24__605.jpg",
                                sourceUrl: "https://google.com",
                                yc: "a Maine Coon cat",
                                hb: "[Image of a Maine Coon cat]",
                                mb: 0
                            }, {
                                wb: "https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-06/Scottish-Fold.jpg?itok=r17XUkvL",
                                sourceUrl: "https://google.com",
                                yc: "a Scottish Fold cat",
                                hb: "[Image of a Scottish Fold cat]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-4",
                        index: 3,
                        textResponse: "Sure, here is a description of Barcelona with images:\n\n**Barcelona is a city of contrasts.** It is a city of old and new, of sea and mountains, of art and architecture.\n\n**In the Gothic Quarter, you can wander through narrow streets and alleyways lined with medieval buildings.** The Pla\u00e7a de Sant Jaume is the heart of the Gothic Quarter, and it is here that you can find the Barcelona City Hall and the Palau de la Generalitat de Catalunya, the seat of the Catalan government.\n\n[Image of the Gothic Quarter]\n\n**Las Ramblas is a wide boulevard that runs through the heart of Barcelona.** It is lined with shops, restaurants, and street performers. The Ramblas is a great place to people-watch and soak up the atmosphere of the city.\n\n[Image of Las Ramblas]\n\n**The Barceloneta Beach is a popular spot for swimming, sunbathing, and people-watching.** It is a long stretch of sandy beach that is perfect for relaxing in the sun or taking a dip in the Mediterranean Sea.\n\n[Image of the Barceloneta Beach]\n\n**Barcelona is also a city of art and architecture.** Antoni Gaud\u00ed, one of the most famous architects of all time, left his mark on the city with his unique and whimsical buildings. The Sagrada Familia, Park G\u00fcell, and Casa Mil\u00e0 are just a few of Gaud\u00ed's masterpieces.\n\n[Image of the Sagrada Familia]\n\n**Barcelona is a city that has something to offer everyone.** Whether you are interested in history, art, architecture, or simply want to relax on the beach, Barcelona is the perfect place to visit.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://assets2.devourtours.com/wp-content/uploads/Gothic-Quarter-in-Barcelona-1.png",
                                sourceUrl: "https://google.com",
                                yc: "Gothic Quarter",
                                hb: "[Image of the Gothic Quarter]",
                                mb: 0
                            }, {
                                wb: "https://c8.alamy.com/comp/MTTM1R/las-ramblas-barcelona-stalls-along-the-busy-rambla-sant-josep-barcelona-catalunya-spain-MTTM1R.jpg",
                                sourceUrl: "https://google.com",
                                yc: "Image of Las Ramblas",
                                hb: "[Image of Las Ramblas]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/951974648/photo/barceloneta-beach-in-barcelona-with-colorful-sky-at-sunrise-seafront-beach-coast-in-spain.jpg?s=612x612&w=0&k=20&c=h7AZ-chjljk4TnJOf75x8xKqlwtDULBk_Cwf9pOzidQ=",
                                sourceUrl: "https://google.com",
                                yc: "Barceloneta Beach",
                                hb: "[Image of the Barceloneta Beach]",
                                mb: 0
                            }, {
                                wb: "https://media.istockphoto.com/id/1130443789/photo/sagrada-familia-basilica-in-barcelona.jpg?b=1&s=170667a&w=0&k=20&c=Ufz9DWJ-ylTv1YeBrsy48jKZJ6EUm2dOEg38aT8j5X0=",
                                sourceUrl: "https://google.com",
                                yc: "Sagrada Familia",
                                hb: "[Image of the Sagrada Familia]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-5",
                        index: 4,
                        textResponse: "Sure, here are the top 5 most popular and in-demand professions, along with a relevant image for each:\n\n* **Healthcare**\n[Image of Doctor]\n\nThe healthcare industry is always in need of qualified workers, and there are a variety of positions available, from doctors and nurses to pharmacists and physical therapists.\n\n* **Technology**\n[Image of Software Developer]\n\nThe technology industry is growing rapidly, and there are many opportunities for software developers, engineers, and other tech professionals.\n\n* **Education**\n[Image of Teacher]\n\nThis field is essential to society, and there is a high demand for teachers, administrators, and other education professionals.\n\n* **Business**\n[Image of Businesswoman]\n\nThere are many different types of businesses, and each one needs a variety of workers, from accountants and lawyers to marketers and sales representatives.\n\n* **Government**\n[Image of Police Officer]\n\nThe government employs people in a wide range of fields, from law enforcement and social services to education and healthcare.\n\nUltimately, the best profession for you is the one that you are passionate about and that allows you to use your skills and talents to make a difference in the world.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://images.theconversation.com/files/304957/original/file-20191203-66986-im7o5.jpg",
                                sourceUrl: "https://google.com",
                                title: "Doctor",
                                hb: "[Image of Doctor]",
                                mb: 0
                            }, {
                                wb: "https://bairesdev.mo.cloudinary.net/blog/2021/09/software-developer-1.jpg",
                                sourceUrl: "https://google.com",
                                title: "Software Developer",
                                hb: "[Image of Software Developer]",
                                mb: 0
                            }, {
                                wb: "https://apicms.thestar.com.my/uploads/images/2022/05/15/1585587.jpg",
                                sourceUrl: "https://google.com",
                                title: "Teacher",
                                hb: "[Image of Teacher]",
                                mb: 0
                            }, {
                                wb: "https://img.freepik.com/free-photo/smiling-confident-businesswoman-posing-with-arms-folded_1262-20950.jpg",
                                sourceUrl: "https://google.com",
                                title: "Businesswoman",
                                hb: "[Image of Businesswoman]",
                                mb: 0
                            }, {
                                wb: "https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/text-with-image-square/officer-andrew-stock.jpg",
                                sourceUrl: "https://google.com",
                                title: "Police Officer",
                                hb: "[Image of Police Officer]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-6",
                        index: 5,
                        textResponse: "Sure, here are 2 pairs of cute cats: [2 Images of cute cats][2 Images of cute cats]\n\n and here are another 2 pairs of cute cats: [2 Images of cute cats][2 Images of cute cats]",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 0
                            }, {
                                wb: "https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&w=1000&q=80",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 0
                            }, {
                                wb: "https://cdn-prd.content.metamorphosis.com/wp-content/uploads/sites/6/2022/12/shutterstock_781327003-1.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1
                            }, {
                                wb: "https://i.pinimg.com/originals/9f/16/32/9f163259165a9031b62fbd8c38746645.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQapeHjw8h0HNkDurVGTByJbE8_vAG3_123Fg&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 2
                            }, {
                                wb: "https://wallpaperaccess.com/full/94041.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 2
                            }, {
                                wb: "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2015_25/1082591/150618-cat.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFYOe9Z04-TFb3_D-pfTT7J7R6SWkSTxifvQ&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-7",
                        index: 6,
                        textResponse: "Sure, here are some cute cats: [2 Images of cute cats][2 Images of cute cats]\n\n[2 Images of cute cats][2 Images of cute cats]",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 0
                            }, {
                                wb: "",
                                errorMessage: "Couldn't load.",
                                hb: "[2 Images of cute cats]",
                                mb: 0
                            }, {
                                wb: "https://cdn-prd.content.metamorphosis.com/wp-content/uploads/sites/6/2022/12/shutterstock_781327003-1.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1
                            }, {
                                wb: "https://i.pinimg.com/originals/9f/16/32/9f163259165a9031b62fbd8c38746645.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQapeHjw8h0HNkDurVGTByJbE8_vAG3_123Fg&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 2
                            }, {
                                wb: "https://wallpaperaccess.com/full/94041.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 2
                            }, {
                                wb: "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2015_25/1082591/150618-cat.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFYOe9Z04-TFb3_D-pfTT7J7R6SWkSTxifvQ&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-8",
                        index: 7,
                        textResponse: "Sure, here are some cute cats: [2 Images of cute cats][2 Images of cute cats]\n\n and here are more cute cats: [2 Images of cute cats][2 Images of cute cats]",
                        Kb: {
                            ad: !1,
                            hc: [{
                                wb: "https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 0,
                                title: "cute cat #1"
                            }, {
                                wb: "https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGNhdHxlbnwwfHwwfHw%3D&w=1000&q=80",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 0
                            }, {
                                wb: "https://cdn-prd.content.metamorphosis.com/wp-content/uploads/sites/6/2022/12/shutterstock_781327003-1.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1,
                                title: "cute cat #3 with a very very very long title"
                            }, {
                                wb: "https://i.pinimg.com/originals/9f/16/32/9f163259165a9031b62fbd8c38746645.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 1
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQapeHjw8h0HNkDurVGTByJbE8_vAG3_123Fg&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 2,
                                title: "cute cat #5"
                            }, {
                                wb: "",
                                sourceUrl: "",
                                yc: "",
                                hb: "[2 Images of cute cats]",
                                mb: 2,
                                errorMessage: "Can't find image."
                            }, {
                                wb: "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2015_25/1082591/150618-cat.jpg",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3,
                                title: "cute cat #7"
                            }, {
                                wb: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFYOe9Z04-TFb3_D-pfTT7J7R6SWkSTxifvQ&usqp=CAU",
                                sourceUrl: "https://google.com",
                                yc: "cute cats",
                                hb: "[2 Images of cute cats]",
                                mb: 3
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_DEVICE",
                        og: !0,
                        Cx: ""
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "images_advanced":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Sure, here are two types of cats with images:\n\n[Image of a Siamese cat]\n\nSiamese cats are a breed of domestic cat that is known for its distinctive coloring and personality. They are typically slender and muscular, with long, silky fur that is short on the head and legs and longer on the body. Siamese cats come in a variety of colors, but the most common are seal point, chocolate point, blue point, and lilac point. They have almond-shaped eyes that are usually blue, and they have a very vocal personality. Siamese cats are known for being very affectionate and playful, and they make great companions for people of all ages.\n\n[Image of a Persian cat]\n\nPersian cats are a breed of domestic cat that is known for its long, luxurious fur. They are typically large and round, with a short, stocky body and a large head. Persian cats have a wide variety of colors, but the most common are black, white, brown, and blue. They have large, round eyes that are usually blue, and they have a very gentle and affectionate personality. Persian cats are known for being very good lap cats, and they make great companions for people who love to cuddle.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://www.google.com/url?sa=i&url=https%3A%2F%2Fencrypted-tbn2.gstatic.com%2Flicensed-image%3Fq%3Dtbn%3AANd9GcS7doMt2tKaUzd8YdXlqTvGrFQOv4OVjtY0DRD12KLdbPTxGuBHxiyZC38iNkIKn8psrwWdSUPlwdroJkw&psig=AOvVaw13Bgp6twa10v2XUKFgBsju&ust=1683540805584000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOij5bD84v4CFQAAAAAdAAAAABAE",
                                sourceUrl: "https://google.com",
                                title: "Siamese cat",
                                hb: "[Image of a Siamese cat]",
                                mb: 0
                            }, {
                                wb: "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQidlV9jhpM0RqJNFDVt0FReCLbVtSLC-DadcjGHwQzPpcg-rzdWH6qAqMDyeRrBQZuBcLF5vTK0sTElT8",
                                sourceUrl: "https://google.com",
                                title: "Persian cat",
                                hb: "[Image of a Persian cat]",
                                mb: 0
                            }]
                        },
                        Cd: {
                            Ce: pr([[{
                                start: 100,
                                end: 140
                            }], [{
                                start: 400,
                                end: 460
                            }], [{
                                start: 600,
                                end: 666
                            }]]),
                            hg: {
                                status: 0
                            },
                            mode: 0
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Sure, here are some images of cats, along with a description of each kind:\n\n* **Persian cats** are known for their long, thick fur and round faces. They are a popular breed of cat, and are often described as being gentle and affectionate.\n[Image of a Persian cat]\n\n* **Abyssinian cats** are known for their sleek, athletic bodies and distinctive ticking fur. They are a playful and intelligent breed of cat, and are often described as being curious and inquisitive.\n[Image of an Abyssinian cat]\n\n* **Siamese cats** are known for their distinctive markings, which consist of dark points on the face, ears, legs, and tail. They are a vocal and affectionate breed of cat, and are often described as being loyal and devoted.\n[Image of a Siamese cat]\n\n* **Maine Coon cats** are the largest breed of domestic cat. They are known for their long, thick fur, bushy tails, and tufted ears. They are a gentle and affectionate breed of cat, and are often described as being laid-back and easygoing.\n[Image of a Maine Coon cat]\n\n* **Scottish Fold cats** are known for their folded ears, which give them a distinctive appearance. They are a gentle and affectionate breed of cat, and are often described as being playful and curious.\n[Image of a Scottish Fold cat]\n\nThese are just a few of the many different breeds of cats that exist. Each breed has its own unique set of characteristics, making them all special in their own way.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://www.thesprucepets.com/thmb/5OSN_p9hUfPssKsJORQDGnAz_tQ=/1963x0/filters:no_upscale():strip_icc()/GettyImages-181861505-4e63227ed0a14dc9bfe86848ef54caf3.jpg",
                                sourceUrl: "https://google.com",
                                title: "Persian cat",
                                hb: "[Image of a Persian cat]",
                                mb: 0
                            }, {
                                wb: "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRArbVS6wpy-yY7IGo8T1zWrr0wl3mpQOhoqpMEtygh_XyWqO7m_3gyyJsfrFF1lP6hLcv_Uf7HjOAdD7M",
                                sourceUrl: "https://google.com",
                                title: "Abyssinian cat",
                                hb: "[Image of an Abyssinian cat]",
                                mb: 0
                            }, {
                                wb: "https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-06/Siamese-Cat_0.jpg?itok=Qy1J6ZDS",
                                sourceUrl: "https://google.com",
                                title: "Siamese cat",
                                hb: "[Image of a Siamese cat]",
                                mb: 0
                            }, {
                                wb: "https://static.boredpanda.com/blog/wp-content/uploads/2015/11/maine-coon-cats-24__605.jpg",
                                sourceUrl: "https://google.com",
                                title: "Maine Coon cat",
                                hb: "[Image of a Maine Coon cat]",
                                mb: 0
                            }, {
                                wb: "https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-06/Scottish-Fold.jpg?itok=r17XUkvL",
                                sourceUrl: "https://google.com",
                                title: "Scottish Fold cat",
                                hb: "[Image of a Scottish Fold cat]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-3",
                        index: 2,
                        textResponse: "Sure, here are some funny cartoons of vegetables:\n\n* **Carrot:**\n[Image of Carrot cartoon where a carrot is wearing sunglasses and a hat]\n\n> A carrot is running away from a rabbit. The rabbit is chasing the carrot because it wants to eat it. The carrot is trying to escape because it knows that the rabbit will eat it if it catches it.\n\n* **Potato:**\n[Image of Potato cartoon where a potato is wearing a cowboy hat and boots]\n> A carrot is running away from a rabbit. The rabbit is chasing the carrot because it wants to eat it. The carrot is trying to escape because it knows that the rabbit will eat it if it catches it.\n\n* **Tomato:**\n[Image of Tomato cartoon where a tomato is wearing a cape and fighting crime]\n\n> A carrot is running away from a rabbit. The rabbit is chasing the carrot because it wants to eat it. The carrot is trying to escape because it knows that the rabbit will eat it if it catches it.\n\n* **Broccoli:**\n[Image of Broccoli cartoon where a broccoli is wearing a crown and is being treated like a king]\n\n> A carrot is running away from a rabbit. The rabbit is chasing the carrot because it wants to eat it. The carrot is trying to escape because it knows that the rabbit will eat it if it catches it.\n\n* **Cucumber:**\n[Image of Cucumber cartoon where a cucumber is swimming in a pool and having a great time]\n\n> A carrot is running away from a rabbit. The rabbit is chasing the carrot because it wants to eat it. The carrot is trying to escape because it knows that the rabbit will eat it if it catches it.\n\nI hope you enjoy these cartoons!",
                        Kb: {
                            ad: !1,
                            hc: [{
                                wb: "https://image.spreadshirtmedia.com/image-server/v1/compositions/T210A1PA4301PT17X12Y16D1042514619W30698H36838/views/1,width=550,height=550,appearanceId=1,backgroundColor=FFFFFF,noPt=true/humorous-carrots-plants-beets-leeks-sunglasses-mens-t-shirt.jpg",
                                sourceUrl: "https://google.com",
                                title: "Carrot cartoon where a carrot is wearing sunglasses and a hat",
                                hb: "[Image of Carrot cartoon where a carrot is wearing sunglasses and a hat]",
                                mb: 0
                            }, {
                                wb: "http://t0.gstatic.com/images?q=tbn:ANd9GcTzicK6LpSvj_tPTr7SZYtL6DlR3QRshARS1_BOHy0RQtDF2yc&s",
                                sourceUrl: "https://google.com",
                                title: "Potato cartoon where a potato is wearing a cowboy hat and boots",
                                hb: "[Image of Potato cartoon where a potato is wearing a cowboy hat and boots]",
                                mb: 0
                            }, {
                                wb: "https://mario.wiki.gallery/images/b/b2/MPS_Shy_Guy_Artwork.png",
                                sourceUrl: "https://google.com",
                                title: "Tomato cartoon where a tomato is wearing a cape and fighting crime",
                                hb: "[Image of Tomato cartoon where a tomato is wearing a cape and fighting crime]",
                                mb: 0
                            }, {
                                wb: "https://rlv.zcache.co.uk/happy_birthday_broc_star_broccoli-r27f4dfc72ecc49af9f431f7b4059a16b_djy5o_644.jpg",
                                title: "Broccoli cartoon where a broccoli is wearing a crown and is being treated like a king",
                                hb: "[Image of Broccoli cartoon where a broccoli is wearing a crown and is being treated like a king]",
                                mb: 0
                            }, {
                                wb: "http://t0.gstatic.com/images?q=tbn:ANd9GcRh4h1ZmuzNbXF6PP3ckXL8MOfgTab3h0Z2PKVvOuIqRr1TlEs&s",
                                sourceUrl: "https://google.com",
                                title: "Cucumber cartoon where a cucumber is swimming in a pool and having a great time",
                                hb: "[Image of Cucumber cartoon where a cucumber is swimming in a pool and having a great time]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-4",
                        index: 3,
                        textResponse: "This is a response with a citations inside image tags:\n\nHere is an image with a citation around the image:\n\n[Image of the Dolder Grand hotel]\n\nThis is Dodler.\n\nAnd this is an image with citation end in it: [Image of the Dolder Grand hotel]\n\nAnd this is an image with citation start in it:\n\n[Image of the Baur au Lac hotel] This hotel is also nice.\n\nAnd this is an image with a citation located inside of its tag:\n\nHere is the picture: [Image of the Baur au Lac hotel]",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/295103799.jpg?k=5c70abbc799492a9f59146fd0136c6406fdeb97777b560501b8519729f32efed&o=&hp=1",
                                sourceUrl: "https://google.com",
                                title: "Dolder Grand hotel",
                                hb: "[Image of the Dolder Grand hotel]",
                                mb: 0
                            }, {
                                wb: "https://meeting.zuerich.com/sites/default/files/web-dolder-zurich.jpg",
                                sourceUrl: "https://google.com",
                                title: "Dolder Grand hotel",
                                hb: "[Image of the Dolder Grand hotel]",
                                mb: 1
                            }, {
                                wb: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/185096503.jpg?k=1dceef7a5c802f8fbdc8297ce82d2d0b25a45a03c3986e503b318a9fb51b8a5c&o=&hp=1",
                                sourceUrl: "https://google.com",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 0
                            }, {
                                wb: "https://www.bauraulac.ch/upload/rm/bauraulac-lehall-header-2-3.jpg?_=1620988536000",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 1
                            }]
                        },
                        Cd: {
                            Ce: pr([[{
                                start: 100,
                                end: 150
                            }], [{
                                start: 190,
                                end: 230
                            }], [{
                                start: 315,
                                end: 340
                            }], [{
                                start: 445,
                                end: 455
                            }]]),
                            hg: {
                                status: 0
                            },
                            mode: 0
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, Ca",
                        Rf: "SWML_DESCRIPTION_BASED_ON_YOUR_PLACES_WORK",
                        og: !1,
                        Cx: ""
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "images_in_tables":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Sure, here is a list of the 3 most popular hotels in Zurich, with the hotel description and hotel image:\n\n| Hotel | Description | Main Image |\n|---|---|---|\n| **The Dolder Grand** | The Dolder Grand is a [Image of the Dolder Grand hotel] luxury hotel located on the Dolder mountain, overlooking Zurich. It offers stunning views of the city and the Alps, as well as a variety of amenities, including a spa, a golf course, and several restaurants. The hotel has a modern and elegant design, and the staff is highly attentive and professional. | [Image of the Dolder Grand hotel] |\n| **The Baur au Lac** | The Baur au Lac is another luxury hotel located in the heart of Zurich. [Image of the Baur au Lac hotel][Image of the Baur au Lac hotel] [Image of the Baur au Lac hotel] It has been in operation since 1844 and is known for its elegant accommodations, its Michelin-starred restaurant, and its world-class service. The hotel has a classic and timeless design, and the staff is incredibly attentive and friendly. | [Image of the Baur au Lac hotel] |\n| **The W Zurich** | The W Zurich is a modern, stylish hotel located in the trendy Langstrasse district of Zurich. It offers a rooftop bar with panoramic views, a fitness center, and a spa. The hotel has a vibrant and energetic atmosphere, and the staff is friendly and welcoming. | [Image of the W Zurich hotel] |\n\nI hope this helps!",
                        Kb: {
                            ad: !1,
                            hc: [{
                                wb: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/295103799.jpg?k=5c70abbc799492a9f59146fd0136c6406fdeb97777b560501b8519729f32efed&o=&hp=1",
                                sourceUrl: "https://google.com",
                                title: "Dolder Grand hotel",
                                hb: "[Image of the Dolder Grand hotel]",
                                mb: 0
                            }, {
                                wb: "https://meeting.zuerich.com/sites/default/files/web-dolder-zurich.jpg",
                                sourceUrl: "https://google.com",
                                title: "Dolder Grand hotel",
                                hb: "[Image of the Dolder Grand hotel]",
                                mb: 1
                            }, {
                                wb: "https://cf.bstatic.com/xdata/images/hotel/max1024x768/185096503.jpg?k=1dceef7a5c802f8fbdc8297ce82d2d0b25a45a03c3986e503b318a9fb51b8a5c&o=&hp=1",
                                sourceUrl: "https://google.com",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 0
                            }, {
                                wb: "https://www.bauraulac.ch/upload/rm/bauraulac-lehall-header-2-3.jpg?_=1620988536000",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 1
                            }, {
                                wb: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/7c/0c/50/baur-au-lac.jpg?w=700&h=-1&s=1",
                                sourceUrl: "https://google.com",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 2
                            }, {
                                wb: "https://www.zuerich.com/sites/default/files/image/2022/web_zuerich_hotel_baur_au_lac_1280x960_43070.jpg",
                                sourceUrl: "https://google.com",
                                title: "Baur au Lac hotel",
                                hb: "[Image of the Baur au Lac hotel]",
                                mb: 3
                            }, {
                                wb: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/de/73/b7/aussenansicht.jpg?w=1200&h=-1&s=1",
                                sourceUrl: "https://google.com",
                                title: "Z\u00fcrich Hotel",
                                hb: "[Image of the W Zurich hotel]",
                                mb: 0
                            }, {
                                wb: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/de/73/b7/aussenansicht.jpg?w=1200&h=-1&s=1",
                                sourceUrl: "https://google.com",
                                title: "Z\u00fcrich Hotel",
                                hb: "[Image of the W Zurich hotel]",
                                mb: 1
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Sure, here is a table of the flowers I mentioned in my previous response:\n\n| Flower | Type | Image |\n|---|---|---|\n| Roses | Cut flowers | [Image of Vase of roses in a table] |\n| Wildflowers | Cut flowers | [Image of Bowl of wildflowers in a table] |\n| Succulents | Live plants | [Image of Succulent centerpiece in a table] |\n| Air plants | Live plants | [Image of Terrarium of air plants in a table] |\n\nI hope this is helpful!",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://cdn.shopify.com/s/files/1/2438/3171/products/Pfingstrosen-coral-vase-medium-bg_grey_1080x.jpg?v=1650447391",
                                sourceUrl: "https://google.com",
                                title: "Vase of roses in a table",
                                hb: "[Image of Vase of roses in a table]",
                                mb: 0
                            }, {
                                wb: "https://cdn.shopify.com/s/files/1/0748/9875/products/PastelWildflowersBowlArrangementSmall_4.jpg?v=1651510250&width=1400",
                                sourceUrl: "https://google.com",
                                title: "Bowl of wildflowers in a table",
                                hb: "[Image of Bowl of wildflowers in a table]",
                                mb: 0
                            }, {
                                wb: "https://i.pinimg.com/originals/22/5b/5d/225b5dc314b05bf5b75734aa1576242e.jpg",
                                sourceUrl: "https://google.com",
                                title: "Succulent centerpiece in a table",
                                hb: "[Image of Succulent centerpiece in a table]",
                                mb: 0
                            }, {
                                wb: "https://cdn.shopify.com/s/files/1/0157/4262/products/Table_top_terrarium_e7fad649-dbbd-42fe-996b-5ea36323225a_1800x1800.jpg?v=1643394869",
                                title: "Terrarium of air plants in a table",
                                hb: "[Image of Terrarium of air plants in a table]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-3",
                        index: 2,
                        textResponse: "Here is a table of flowers with their names, colors, and meanings:\n\n| Flower | Color | Meaning |\n|---|---|---|\n| Rose | Red | Love, passion, romance, passion, romance, passion, romance, passion, romance .[Image of Vase of roses in a table]\n| Lily of the valley | White | Purity, sweetness, humility .[Image of Bowl of wildflowers in a table]\n| Orchid | White, pink, purple, blue | Elegance, luxury, beauty .[Image of Succulent centerpiece in a table]\n| Snapdragon | Red, orange, yellow, pink, white | Creativity, imagination, playfulness .[Image of Terrarium of air plants in a table]\n\nThese are just a few of the many beautiful flowers that are available. When choosing flowers, it is important to consider the occasion, the recipient's preferences, and the overall look you are trying to achieve.",
                        Kb: {
                            ad: !0,
                            hc: [{
                                wb: "https://cdn.shopify.com/s/files/1/2438/3171/products/Pfingstrosen-coral-vase-medium-bg_grey_1080x.jpg?v=1650447391",
                                sourceUrl: "https://google.com",
                                title: "Vase of roses in a table",
                                hb: "[Image of Vase of roses in a table]",
                                mb: 0
                            }, {
                                wb: "https://cdn.shopify.com/s/files/1/0748/9875/products/PastelWildflowersBowlArrangementSmall_4.jpg?v=1651510250&width=1400",
                                sourceUrl: "https://google.com",
                                title: "Bowl of wildflowers in a table",
                                hb: "[Image of Bowl of wildflowers in a table]",
                                mb: 0
                            }, {
                                wb: "https://i.pinimg.com/originals/22/5b/5d/225b5dc314b05bf5b75734aa1576242e.jpg",
                                sourceUrl: "https://google.com",
                                title: "Succulent centerpiece in a table",
                                hb: "[Image of Succulent centerpiece in a table]",
                                mb: 0
                            }, {
                                wb: "https://cdn.shopify.com/s/files/1/0157/4262/products/Table_top_terrarium_e7fad649-dbbd-42fe-996b-5ea36323225a_1800x1800.jpg?v=1643394869",
                                title: "Terrarium of air plants in a table",
                                hb: "[Image of Terrarium of air plants in a table]",
                                mb: 0
                            }]
                        },
                        Vb: [],
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, Ca",
                        Rf: "SWML_DESCRIPTION_BASED_ON_YOUR_PLACES_WORK",
                        og: !1,
                        Cx: ""
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "tool_disclaimer":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Hi there!\nhttp://googleusercontent.com/tool_disclaimer_content/1\n\nHere is some text that should go after the attachment anchor.",
                        Vb: [],
                        Kb: {
                            hc: [],
                            ad: !1,
                            nY: [{
                                hb: "http://googleusercontent.com/tool_disclaimer_content/1",
                                mb: 0,
                                s8: "Bard doesn't always get it right. Be sure to check the following flight and hotel details:\n\nGoogle Flights\nRound trip \u2022 _SJC, SFO - MIA_ \u2022 _Sept 15 - Sept 18_\nRound trip \u2022 SJC, SFO - LHR \u2022 _July 1 - July 14_\n\nGoogle Hotels\nMiami \u2022 _Sep 15 - Sept 18_ \u2022 2 guests\nLondon \u2022 _July 1 - July 14_ \u2022 2 guests",
                                zT: 1
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [],
                    Vc: [],
                    Ad: "response-" + b + "-1"
                }));
            case "maps_basic":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some options for grocery stores near sunnyvale:\n\n1. Whole Foods Market: Eco-minded chain with natural & organic grocery items, housewares & other products (most sell wine)., Rating: 4.5\n\n2. Sprouts Farmers Market: Specialty chain offering a range of natural & organic grocery items, including own-brand goods., Rating: 4.4\n\nhttp://googleusercontent.com/map_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [{
                                hb: "http://googleusercontent.com/map_content/1",
                                mb: 0,
                                title: "maps label for XXX",
                                Zl: {
                                    displayName: "Google Maps",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/maps/v7/192px.svg"
                                },
                                Kf: 1,
                                places: [{
                                    id: "ChIJC55dsuqAhYARQApjF1OPPWU",
                                    displayName: "Whole Foods Market",
                                    location: {
                                        lat: 37.3741134,
                                        lng: -122.0508087
                                    },
                                    kk: 4,
                                    Ul: 3,
                                    priceLevel: "$$$",
                                    Vt: "Grocery store",
                                    openNow: !1,
                                    Dw: "https://maps.google.com/"
                                }, {
                                    id: "ChIJ-w2D4zuHhYAROYAF0fL-EXo",
                                    displayName: "Taqueria Los Mayas",
                                    location: {
                                        lat: 37.367464,
                                        lng: -122.030256
                                    },
                                    kk: 4.3,
                                    Ul: 203,
                                    priceLevel: "$$",
                                    Vt: "Mexican",
                                    openNow: !0,
                                    Dw: "https://maps.google.com/"
                                }, {
                                    id: "ChIJd8AKgMaHhYARYKd_1_H9A6E",
                                    displayName: "Sephora",
                                    location: {
                                        lat: 37.3704531,
                                        lng: -122.0535653
                                    },
                                    Vt: "Cosmetics",
                                    openNow: !1,
                                    Dw: "https://maps.google.com/"
                                }]
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Here are some options for grocery stores near sunnyvale:\n\nhttp://googleusercontent.com/map_content/1\n\n1. Whole Foods Market: Eco-minded chain with natural & organic grocery items, housewares & other products (most sell wine)., Rating: 4.5\n\n2. Sprouts Farmers Market: Specialty chain offering a range of natural & organic grocery items, including own-brand goods., Rating: 4.4\n\nHere are some options for grocery stores near seattle:\n\nhttp://googleusercontent.com/map_content/2\n\n1. Metropolitan Market Queen Annes\n\n2. Grocery Outlet",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [{
                                hb: "http://googleusercontent.com/map_content/1",
                                mb: 0,
                                title: "maps label for XXX",
                                Zl: {
                                    displayName: "Google Maps",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/maps/v7/192px.svg"
                                },
                                Kf: 1,
                                places: [{
                                    id: "l_1",
                                    displayName: "Whole Foods Market",
                                    location: {
                                        lat: 37.3741134,
                                        lng: -122.0508087
                                    }
                                }, {
                                    id: "l_2",
                                    displayName: "Sprouts Farmers Market",
                                    location: {
                                        lat: 37.367464,
                                        lng: -122.030256
                                    }
                                }, {
                                    id: "l_3",
                                    displayName: "Sprouts Farmers Market",
                                    location: {
                                        lat: 37.3704531,
                                        lng: -122.0535653
                                    }
                                }]
                            }, {
                                hb: "http://googleusercontent.com/map_content/2",
                                mb: 0,
                                title: "maps label for XXX",
                                Zl: {
                                    displayName: "Google Maps",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/maps/v7/192px.svg"
                                },
                                Kf: 1,
                                places: [{
                                    id: "l_4",
                                    displayName: "Metropolitan Market Queen Annes",
                                    location: {
                                        lat: 47.552835,
                                        lng: -122.379571
                                    }
                                }, {
                                    id: "l_5",
                                    displayName: "Grocery Outlet",
                                    location: {
                                        lat: 47.552,
                                        lng: -122.37957189
                                    }
                                }]
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "processing_state":
                return oS(this, rr(a, b), !0);
            case "safety_disclaimer":
                return d = {
                    id: "response-" + b + "-1",
                    index: 0,
                    textResponse: c ? "Response to " + c : "",
                    Vb: [],
                    Kb: {
                        ad: !1,
                        hc: [],
                        jK: 2
                    },
                    oc: 0,
                    Cc: !1,
                    Gc: !1
                },
                oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: c ? [d] : [],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: c ? "response-" + b + "-1" : void 0
                }));
            case "shopping_multiple_products":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some shopping products to consider:\n[products]\nThis is all.",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            BN: [{
                                title: "Brewista Smart Pour 1.2L",
                                hb: "[products]",
                                mb: 0,
                                Wk: "56.70 USD",
                                rating: 4.9,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRflgXLg5t_5pXwXxfsE1bPOsatPeNH3HYpqPCrMMvsrVDrCu_SfelEzWKXD-_D5zjgxvl5nW1e0K5FGypq3o7Wr1BxOJ6L0y-1E2mAgr4AVK6Agpa3L6zl2Sg6tlEvrg6MoTQ&usqp=CAc"
                            }, {
                                title: "Sunbeam 1.2L Cordless",
                                hb: "[products]",
                                mb: 0,
                                Wk: "78.11 USD",
                                rating: 4.7,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU57FMjYciT8TEP01E6fpLIU_NFv7kBelWbKPjDDNi&s"
                            }, {
                                title: "Bodum Variable Temperature Electric Kettle",
                                hb: "[products]",
                                mb: 0,
                                Wk: "29.67 USD",
                                rating: 2.2,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU57FMjYciT8TEP01E6fpLIU_NFv7kBelWbKPjDDNi&s"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_YOUR_DEFAULT_LOCATION",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "shopping_single_product":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "We can also add some products individually:\n[inline product Brewista Smart Pour]\nwith some text in between [inline product Bodum Variable Temperature Electric Kettle].\nWe can also have the same thing twice [inline product Bodum Variable Temperature Electric Kettle]. Sometimes\nthey are invalid\n[inline product Invalid Product Name]\nor after.",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            BN: [{
                                title: "Brewista Smart Pour 1.2L",
                                hb: "[inline product Brewista Smart Pour]",
                                mb: 0,
                                inline: !0,
                                Wk: "56.70 USD",
                                rating: 4.9,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRflgXLg5t_5pXwXxfsE1bPOsatPeNH3HYpqPCrMMvsrVDrCu_SfelEzWKXD-_D5zjgxvl5nW1e0K5FGypq3o7Wr1BxOJ6L0y-1E2mAgr4AVK6Agpa3L6zl2Sg6tlEvrg6MoTQ&usqp=CAc"
                            }, {
                                title: "Sunbeam 1.2L Cordless",
                                hb: "[inline product Sunbeam Cordless]",
                                mb: 0,
                                inline: !0,
                                Wk: "78.11 USD",
                                rating: 4.7,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU57FMjYciT8TEP01E6fpLIU_NFv7kBelWbKPjDDNi&s"
                            }, {
                                title: "Bodum Variable Temperature Electric Kettle",
                                hb: "[inline product Bodum Variable Temperature Electric Kettle]",
                                mb: 1,
                                inline: !0,
                                Wk: "29.67 USD",
                                rating: 2.2,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU57FMjYciT8TEP01E6fpLIU_NFv7kBelWbKPjDDNi&s"
                            }, {
                                title: "Bodum Variable 2nd Version",
                                hb: "[inline product Bodum Variable Temperature Electric Kettle]",
                                mb: 0,
                                inline: !0,
                                Wk: "29.67 USD",
                                rating: 2.2,
                                description: "This kettle has a 1.2L capacity, variable temperature controls, a keep warm function, and a cordless design. It is made of glass and gooseneck spout.",
                                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRU57FMjYciT8TEP01E6fpLIU_NFv7kBelWbKPjDDNi&s"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "title_generation":
                return c = oS,
                d = or(a, _.qr(b, "Title generation test")),
                b = or(a, {
                    ub: "request-" + b,
                    Gb: [],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    TN: "This is a suggested title",
                    Ad: void 0
                }),
                c(this, "" === a.conversationId ? [d, b] : [d], !0, !0);
            case "tool_consent_workspace":
                return d = {
                    id: "response-" + b + "-1",
                    index: 0,
                    textResponse: c ? "Response to " + c : "",
                    Kb: {
                        ad: !1,
                        hc: []
                    },
                    Vb: [],
                    oe: {
                        Fg: "workspace_tool",
                        vc: "Workspace",
                        zc: "https://www.gstatic.com/lamda/images/tools/logo_workspace_v0_d08186dd3411837bf8f15.svg",
                        Lq: 2
                    },
                    oc: 0,
                    Cc: !1,
                    Gc: !1
                },
                oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: c ? [d] : [],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: c ? "response-" + b + "-1" : void 0
                }));
            case "tool_consent_workspace_eecc":
                return d = {
                    id: "response-" + b + "-1",
                    index: 0,
                    textResponse: c ? "Response to " + c : "",
                    Kb: {
                        ad: !1,
                        hc: []
                    },
                    Vb: [],
                    oe: {
                        Fg: "workspace_tool",
                        vc: "Workspace",
                        zc: "https://www.gstatic.com/lamda/images/tools/logo_workspace_v0_d08186dd3411837bf8f15.svg",
                        Lq: 2
                    },
                    oc: 0,
                    Cc: !0,
                    Gc: !1
                },
                oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: c ? [d] : [],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: c ? "response-" + b + "-1" : void 0
                }));
            case "tool_sources_none_workspace_response":
                return oS(this, rr(a, b, g8a, tr(0)));
            case "tool_sources_some":
                return oS(this, rr(a, b, g8a, tr(3)));
            case "tool_sources_many":
                return oS(this, rr(a, b, g8a, tr(15)));
            case "tool_consent_external":
                return d = {
                    id: "response-" + b + "-1",
                    index: 0,
                    textResponse: c ? "Response to " + c : "",
                    Vb: [],
                    Kb: {
                        ad: !1,
                        hc: []
                    },
                    oe: {
                        Fg: "opentable_tool",
                        vc: "Opentable",
                        zc: "https://www.gstatic.com/lamda/images/tools/logo_open_table_df_90183d0d0f3475c927732.svg",
                        Lq: 2
                    },
                    oc: 0,
                    Cc: !1,
                    Gc: !1
                },
                oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: c ? [d] : [],
                    factualityQueries: [],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: c ? "response-" + b + "-1" : void 0
                }));
            case "implicit_code_execution":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: 'Sure, here is the code to generate a plot of y = x^2:\n```python\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n# Create a range of x values\nx = np.linspace(-3, 3, 100)\n\n# Calculate y values\ny = x**2\n\n# Plot the points\nplt.plot(x, y)\n\n# Set the title and axis labels\nplt.title("y = x^2")\nplt.xlabel("x")\nplt.ylabel("y")\n\n# Show the plot\nplt.show()\n```\nHere is a plot of y = x^2:\n\n[image-tag: code_execution_image.png]\n\nHope you find it useful.',
                        Vb: [],
                        Kb: {
                            ad: !1,
                            hc: [],
                            az: [{
                                hb: "[image-tag: code_execution_image.png]",
                                mb: 0,
                                imageUrl: "data:image/jpeg;base64,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"
                            }],
                            Zf: {
                                Ls: "python",
                                Rn: '\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n# Create a range of x values\nx = np.linspace(-3, 3, 100)\n\n# Calculate y values\ny = x**2\n\n# Plot the points\nplt.plot(x, y)\n\n# Set the title and axis labels\nplt.title("y = x^2")\nplt.xlabel("x")\nplt.ylabel("y")\n\n# Show the plot\nplt.show()\n',
                                rK: 0,
                                outcome: 3,
                                Ina: void 0,
                                cA: !0,
                                GS: [{
                                    filename: "data.csv",
                                    Mk: 3,
                                    url: "contribution-dev.usercontent.google.com/download?c=data.csv",
                                    cG: "a1"
                                }],
                                Nna: []
                            }
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Here is a plot of y = x^2:\n\n[image-tag: code_execution_image.png]\n\nHope you find it useful.",
                        Cd: {
                            Ce: pr([[{
                                start: 3,
                                end: 15
                            }], [{
                                start: 3,
                                end: 15
                            }], [{
                                start: 70,
                                end: 90
                            }]]),
                            hg: {
                                status: 0
                            },
                            mode: 0
                        },
                        Vb: tr(10),
                        Kb: {
                            ad: !1,
                            hc: [],
                            az: [{
                                hb: "[image-tag: code_execution_image.png]",
                                mb: 0,
                                imageUrl: "data:image/png;base64,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AA9GAQgAAAAAAAB4MApAAAAAAAAAwINRAMJUmzdv1rBhw1S7dm35+voqLCxMffr00aeffiqHw2F2PKBQ27Zt06hRo1S/fn35+/urbt26uvnmm7V06VKzowGXZLPZ9OSTT8pqteqhhx4yOw7KuYSEBD355JNq3ry5AgICVLFiRbVv316vvfaa0tLSzI4HXNLWrVvVuHFjWSwWJSYmmh0HcJGbm6spU6aoY8eOqly5sipVqqRWrVrppZdeUnJystnxgELl5OTorbfeUvv27VWxYkUFBgYqIiJCEydO1MGDB82O57YshmEYZodA+fTpp59q7Nixstvtha7HxMToxx9/VFBQUCknA4o2ZcoUPfroo7LZbIWujx8/Xu+++64sFkspJwMu7cSJE7r99tu1Zs0aSdK4ceP03nvvmZwK5dWyZcs0dOhQpaSkFLper149/fLLL4qMjCzdYEAxTZ06VRMmTFBOTo4k6ezZswoNDTU5FfA/p06dUv/+/bV169ZC1+vVq6f58+erdevWpZoLuJiUlBT16dNHcXFxha4HBATok08+0R133FHKydwfVwDCFEuWLMkv/5o2baqPP/5YK1eu1DfffKNhw4bJarVq9erVGjVqlNlRgXxff/21xo8fL5vNpiZNmmjatGlatWqV5s6dqz59+kiSJk+erNdff93kpICrxYsXq02bNvnlH2CmtWvX6sYbb1RKSorCwsL02muvaeXKlVqyZIn++c9/KjAwUMeOHVOvXr104MABs+MCTtLT0zV8+HDdf//9+eUfUNbk5eXll39Wq1Xjxo3TwoULtWzZMr344osKCQnRsWPHNGjQIK5eRZly0003KS4uTt7e3nrwwQfzz9t33nlH9erVU1ZWlu666y5t2rTJ7KjuxwBM0KNHD0OSERUVZZw/f95lfdKkSYYkQ5KxY8cOExICznJycoyaNWsakowOHToYmZmZLsfcd999hiQjMDDQSElJMSEl4MputxvPPPOMYbVaDUlG5cqVjVq1ahmSjHHjxpkdD+VQdna2Ub9+fUOSER4ebiQkJLgcs337diMkJMSQZMTExJiQEijczp07jaZNm+a/T42Kisr//dmzZ82OB+SbPHly/rn51Vdfuazv2bPHCAoKMiQZTz/9tAkJAVcrVqzIP29nzpzpsn7u3DkjPDzckGQMHTrUhITujSsAYYqff/5Zn332maZOnVroLb4PPPCAAgICJEmxsbGlHQ9wkZeXp7vvvlthYWH6+OOP88/PP3v11Vfl6+urjIwM/fzzzyakBFydPXtWkydPlsPhUMeOHbVlyxY1btzY7FgoxyZNmqSjR4/K29tbCxcuVI0aNVyOiYqK0ueffy5JWr16tb777rvSjgkUatasWdqzZ498fX01adIkTZ482exIQKFatmypvn37aujQobr11ltd1iMiInT//fdLkr755pvSjgcUqnv37tq1a5fefPNN3XXXXS7rVapU0ejRoyXRE1wJCkCYwt/fXyNHjlTnzp0LXff29pavr68kyWrlNIX5AgMD9cILLyg+Pl6tWrUq9JjKlSurXr16kqRjx46VZjygSGFhYXrzzTc1YcIErV69WvXr1zc7Esq5qVOnSpKGDx9+0ef7DRw4MP99wocfflgq2YBLefbZZ9WrVy+tWbNG48ePNzsOUKTu3bvrl19+0Zw5c4o85o/3tLxvRVnSrFkzPf7440WuV6hQQRI9wZXwNjsAUJivv/5aqampslqtRZaEgBm8vS/+afPcuXOSLvx0Cigr7rnnHrMjAJKkPXv26NChQ5JU6E/2Cxo9erTWrVunlStXKiMjQ4GBgSUdEbiogIAALVmyxOwYQLFd7L3rH8/+430r3EVubq4+++wzSVLXrl1NTuN+qExRZtjtdh04cEDPPvts/jcF48aNU0REhMnJgOJZtWqVkpOTJUnR0dEmpwGAsmf16tWSJF9f32L9gK9nz56SpJycHK1bt65EswFAeTN//nxJUseOHU1OAlxccnKyFi9erJiYGG3dulVVqlTRc889Z3Yst8MVgCgTQkJClJqamv/vVqtVTz31lF588UUTUwHFl5OTo4cffliS1LZtW7Vs2dLkRABQ9pw8eVKSVLduXfn7+1/y+PDwcHl5eclutyshIaGk4wFAuTFnzhwtX75ckjRq1ChzwwBFePfdd/XII484zZo1a6YvvvhCjRo1MimV++IKQJRJhmHozJkzOn/+vNlRgGK59957tX37dknSm2++aXIaACibzpw5I0mqWrVqsY63WCz5t6adPn26xHIBQHmyffv2/MeDdOvWTYMGDTI5EVB8mZmZio+PNzuGW6IARJmwYsUKxcbGasGCBRo7dqysVqumTZumvn37Kj093ex4wEW98MIL+c+iuP/++3XdddeZnAgAAABwdeLECQ0cOFDp6ekKDg7WRx99ZHYkoEjDhg3Txo0btWrVKr333nuKiIjQkSNHdOONN150gxsUjgIQV2zp0qUKCQkp9q8+ffoU+bFat26tDh06aNCgQZo2bZoWLVokHx8fxcbG6o033ijFvxU83dU8b6ULu1n++9//lnThWVWTJ08ujb8GyqGrfe4CZqhevbqk/22YdCmGYSgpKcnptQCAK5OUlKS+ffvq+PHj8vLy0ty5c3neOsq06tWrq3379oqJidG4ceO0detWDRgwQA6HQ/fdd1/+89dRPDwDEFcsLy/P6bl9l5KWllbsY3v16qWHH35Yb7/9tqZOnaoXXnjhSiICLq7meTt37lw9+OCDkqR27drp+++/l4+Pz1/OCBSmJD/nAqWlZs2akqTjx48rOzv7ks8BPHTokOx2uySpVq1aJZ4PADxVenq6BgwYoF27dslqtWrmzJnq27ev2bGAy+Lv768ZM2aofv36On/+vObMmaMHHnjA7FhugysAccX69esnwzCK/Wv9+vWX9fH79+8v6cLzgmj2cbVcrfP2p59+0siRI+VwOBQVFaXFixerUqVKpfy3QXlS0p9zgdLQrVs3SVJubm6xdvX94wH1vr6+6tSpU4lmAwBPlZOTo8GDB2vDhg2SpA8++EAjRowwORVwZapXr6527dpJkvbs2WNyGvdCAQhTLFq0SCNGjJDD4SjymD+vcVUVypIVK1Zo6NChysvLU0REhH799df8h9QDAIrWtGlTNWjQQJLyn516MTNnzpQkde/eXRUrVizJaADgkWw2m2699VYtW7ZMkvTOO+/o3nvvNTkVULgzZ87oueeeu+Tz/f7oCnx9fUsjlsegAESp27hxo/r166fZs2frxx9/LPK4n3/+WZJUp04d3vSjzNiwYYNuvPFGZWdnq0GDBlqyZInCwsLMjgUAbuOPbzxnzZp10Z/c//TTT1q7dq0k6b777iuVbADgSRwOh0aOHKmFCxdKkl5++WVNnDjR3FDARYwePVrPP/+83nrrLRmGUegxZ86c0ebNmyVd+MEiio8CEKWuQ4cOatmypaQLO6aeOHHC5Zjly5fr/ffflySNGTOmVPMBRdm2bZv69++vtLQ01a5dW0uXLlWdOnXMjgUAbmXixImqV6+ebDabBg0apDNnzrgcs3v37vzb07p06aKhQ4eWdkwAcGuGYeiee+7Jv5Lqqaee0lNPPWVyKuDixo4dK0mKi4vT888/77Kek5OjMWPGKCcnRxUrVtStt95a2hHdGpuAwBSffPKJrr32Wp08eVItW7bUE088oejoaGVnZ+uHH37Qxx9/LJvNpiZNmujRRx81Oy6g+Ph49enTR8nJyfL19dXrr7+uc+fOFbmTZVBQELuqAUAh/P39NWvWLPXr108HDhxQq1at9Mgjj6hz587Ky8vTsmXLNGnSJKWnp6tGjRqaPn262ZEBwO08/fTT+Z8/e/furSFDhiguLq7I4yMiIhQUFFRa8YBC3XzzzRoyZIi+++47Pf/889q4caPuvPNO1apVS7t379aUKVO0a9cuSdL//d//8Qz2y2QxirquEihhv/76q2677TalpKQUut6qVSt9++23Cg8PL91gQCFWrFihnj17Fvv47t27a8WKFSUXCPgLevTooZUrV2rcuHF67733zI6Dcmrp0qUaOnRokbtb161bV4sWLVJkZGQpJwOK78/vD86ePavQ0FCTEwEX/PG1vriWL1+uHj16lFwgoJiysrI0cuRIffvtt4Wue3t768UXX9Q//vGPUk7m/rgFGKbp06eP9u/fr3/+859q3ry5/P39FRoaqpiYGE2dOlWxsbGUfwAAeKhevXppz549+vvf/67IyEj5+fmpQoUKateunV599VXt2rWL8g8AgHImICBA33zzjRYuXKhBgwapWrVq8vf3V6NGjXTfffdp8+bNlH9XiCsAAQAAAAAAAA/GFYAAAAAAAACAB6MABAAAAAAAADwYBSAAAAAAAADgwSgAAQAAAAAAAA9GAQgAAAAAAAB4MApAAAAAAAAAwINRAAIAAAAAAAAejAIQAAAAAAAA8GAUgAAAAAAAAIAHowAEAAAAAAAAPBgFIAAAAAAAAODBKAABAAAAAAAAD0YBCAAAAAAAAHgwCkAAAAAAAADAg1EAAgAAAAAAAB6MAhAAAAAAAADwYBSAAAAAAAAAgAejAAQAAAAAAAA8GAUgAAAAAAAA4MEoAAEAAAAAAAAPRgEIAAAAAAAAeDAKQAAAAJSaDRs2yNvbWxaLRa+//nqhxyQmJio0NFQWi0W9e/eWYRilnBIAAMCzUAACAACg1HTs2FGPPvqoJOm5557T3r17XY6ZOHGizp07p6CgIE2fPl0Wi6W0YwIAAHgUi8GPVAEAAFCKsrOz1aZNG+3Zs0ddunTRqlWrZLVe+Ln04sWL1bdvX0nSxx9/rLvvvtvMqAAAAB6BKwABAABQqvz9/TV9+nRZrVatXbtW7733niQpMzNT999/vySpX79+lH8AAABXCVcAAgAAwBSPP/643nrrLQUGBmrHjh36z3/+o7feekshISHauXOnateubXZEAAAAj0ABCAAAAFNkZWWpdevW2rdvn1q3bq0dO3bIbrdr5syZuuuuu8yOBwAA4DEoAAEAAGCatWvXqlu3bnI4HJKkQYMGacGCBSanAgAA8Cw8AxAAAACm6dKli6KiovL//YEHHjAxDQAAgGeiAAQAAIBpZsyYoW3btuX/+xNPPKHc3FwTEwEAAHgeCkAAAACYIiEhQY8++qgkaejQoQoMDNSuXbv0/PPPm5wMAADAs1AAAgAAwBQPPPCAUlJSVKtWLU2fPl0vvPCCJOmNN97Qpk2bTE4HAADgOdgEBAAAAKXuyy+/1LBhwyRJ8+bN05AhQ2S329WpUyfFxcUpKipKcXFx8vX1NTkpAACA++MKQAAAAJSqs2fPavz48ZKkwYMHa8iQIZIkLy8vffzxx/L29taOHTv04osvmhkTAADAY1AAAgAAoFQ99NBDSkxMVFBQkN577z2ntdatW+c/F/C1117Tli1bzIgIAADgUbgFGAAAAKXm+++/z7/ib8qUKXrooYdcjsnKylJUVJQOHjyoli1bKi4uTj4+PqUdFQAAwGNQAAIAAAAAAAAejFuAAQAAAAAAAA9GAQgAAAAAAAB4MApAAAAAAAAAwINRAAIAAAAAAAAejAIQAAAAAAAA8GAUgAAAAAAAAIAHowAEAAAAAAAAPBgFIAAAAAAAAODBKAABAAAAAAAAD0YBCAAAAAAAAHgwCkAAAAAAAADAg1EAAgAAAAAAAB6MAhAAAAAAAADwYBSAAAAAAAAAgAejAAQAAAAAAAA8GAUgAAAAAAAA4MEoAAEAAAAAAAAPRgEIAAAAAAAAeDAKQAAAAAAAAMCDUQACAAAAAAAAHowCEAAAAAAAAPBgFIAAAAAAAACAB6MABAAAAAAAADwYBSAAAAAAAADgwSgAAQAAAAAAAA9GAQgAAAAAAAB4MApAAAAAAAAAwINRAAIAAAAAAAAejAIQAAAAAAAA8GAUgAAAAAAAAIAHowAEAAAAAAAAPBgFIAAAAAAAAODBKAABAAAAAAAAD0YBCAAAAAAAAHgwCkAAAAAAAADAg/0/C2pTVBYmOEgAAAAASUVORK5CYII="
                            }],
                            Zf: {
                                rK: 0,
                                outcome: 3,
                                cA: !0,
                                Ls: "python",
                                Rn: '\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n# Create a range of x values\nx = np.linspace(-3, 3, 100)\n\n# Calculate y values\ny = x**2\n\n# Plot the points\nplt.plot(x, y)\n\n# Set the title and axis labels\nplt.title("y = x^2")\nplt.xlabel("x")\nplt.ylabel("y")\n\n# Show the plot\nplt.show()\n',
                                Ina: {
                                    Ce: pr([[{
                                        start: 3,
                                        end: 15
                                    }], [{
                                        start: 3,
                                        end: 15
                                    }], [{
                                        start: 90,
                                        end: 115
                                    }]]),
                                    hg: {
                                        status: 0
                                    },
                                    mode: 0
                                }
                            }
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-3",
                        index: 2,
                        textResponse: "Here is an interactive plot:\n\n[json-tag: code_execution_json_file.json]\n\n[json-tag: code_execution_json_file_2.json]\n\nHope you find it useful.",
                        Vb: [],
                        Kb: {
                            ad: !1,
                            hc: [],
                            Zf: {
                                outcome: 3,
                                rK: 0,
                                cA: !0,
                                Ls: "python",
                                Rn: '\nfrom bokeh.io import output_file\nfrom bokeh.plotting import figure, show\n\n# prepare some data for an interactive line plot\nx = [1, 2, 3, 4]\ny = [1, 2, 4, 2]\n# create a new plot with a title and axis labels\np = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")\n# add a line renderer with legend and line thickness to the plot\np.line(x, y, legend_label="Temp", line_width=2)\nshow(p)\n',
                                v4: [{
                                    hb: "[json-tag: code_execution_json_file.json]",
                                    mb: 0,
                                    vA: '{"031233e5-8e7e-4ead-92ea-65809a778a8a":{"version":"3.1.0","title":"Bokeh Application","defs":[],"roots":[{"type":"object","name":"Figure","id":"p1001","attributes":{"x_range":{"type":"object","name":"DataRange1d","id":"p1002"},"y_range":{"type":"object","name":"DataRange1d","id":"p1003"},"x_scale":{"type":"object","name":"LinearScale","id":"p1015"},"y_scale":{"type":"object","name":"LinearScale","id":"p1017"},"title":{"type":"object","name":"Title","id":"p1004","attributes":{"text":"Simple line example"}},"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1054","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1048","attributes":{"selected":{"type":"object","name":"Selection","id":"p1050","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1049"},"data":{"type":"map","entries":[["x",[1,2,3,4]],["y",[1,2,4,2]]]}}},"view":{"type":"object","name":"CDSView","id":"p1055","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1056"}}},"glyph":{"type":"object","name":"Line","id":"p1051","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p1052","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p1053","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.2,"line_width":2}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1007","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1033"},{"type":"object","name":"WheelZoomTool","id":"p1034"},{"type":"object","name":"BoxZoomTool","id":"p1035","attributes":{"overlay":{"type":"object","name":"BoxAnnotation","id":"p1036","attributes":{"syncable":false,"level":"overlay","visible":false,"left_units":"canvas","right_units":"canvas","bottom_units":"canvas","top_units":"canvas","line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5}}}},{"type":"object","name":"SaveTool","id":"p1037"},{"type":"object","name":"ResetTool","id":"p1038"},{"type":"object","name":"HelpTool","id":"p1039"}]}},"left":[{"type":"object","name":"LinearAxis","id":"p1026","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1028","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1027"},"axis_label":"y","major_label_policy":{"type":"object","name":"AllLabels","id":"p1029"}}}],"below":[{"type":"object","name":"LinearAxis","id":"p1019","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1021","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1020"},"axis_label":"x","major_label_policy":{"type":"object","name":"AllLabels","id":"p1022"}}}],"center":[{"type":"object","name":"Grid","id":"p1025","attributes":{"axis":{"id":"p1019"}}},{"type":"object","name":"Grid","id":"p1032","attributes":{"dimension":1,"axis":{"id":"p1026"}}},{"type":"object","name":"Legend","id":"p1070","attributes":{"items":[{"type":"object","name":"LegendItem","id":"p1071","attributes":{"label":{"type":"value","value":"Temp"},"renderers":[{"id":"p1054"}]}}]}}]}}],"callbacks":{"type":"map"}}}'
                                }, {
                                    hb: "[json-tag: code_execution_json_file_2.json]",
                                    mb: 0,
                                    vA: '{"ed84829f-d1f2-45b7-a485-163ad6cab281":{"version":"3.1.0","title":"Bokeh Application","defs":[],"roots":[{"type":"object","name":"Row","id":"p1273","attributes":{"children":[{"type":"object","name":"Figure","id":"p1212","attributes":{"width":400,"height":400,"x_range":{"type":"object","name":"DataRange1d","id":"p1214"},"y_range":{"type":"object","name":"Range1d","id":"p1223","attributes":{"start":-10,"end":10}},"x_scale":{"type":"object","name":"LinearScale","id":"p1225"},"y_scale":{"type":"object","name":"LinearScale","id":"p1227"},"title":{"type":"object","name":"Title","id":"p1216"},"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1264","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1209","attributes":{"selected":{"type":"object","name":"Selection","id":"p1211","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1210"},"data":{"type":"map","entries":[["x",{"type":"ndarray","array":{"type":"bytes","data":"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"},"shape":[500],"dtype":"float64","order":"little"}],["y",{"type":"ndarray","array":{"type":"bytes","data":"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"},"shape":[500],"dtype":"float64","order":"little"}]]}}},"view":{"type":"object","name":"CDSView","id":"p1265","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1266"}}},"glyph":{"type":"object","name":"Line","id":"p1261","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.6,"line_width":3}},"nonselection_glyph":{"type":"object","name":"Line","id":"p1262","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.1,"line_width":3}},"muted_glyph":{"type":"object","name":"Line","id":"p1263","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.2,"line_width":3}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1217","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1243"},{"type":"object","name":"WheelZoomTool","id":"p1244"},{"type":"object","name":"BoxZoomTool","id":"p1245","attributes":{"overlay":{"type":"object","name":"BoxAnnotation","id":"p1246","attributes":{"syncable":false,"level":"overlay","visible":false,"left_units":"canvas","right_units":"canvas","bottom_units":"canvas","top_units":"canvas","line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5}}}},{"type":"object","name":"SaveTool","id":"p1247"},{"type":"object","name":"ResetTool","id":"p1248"},{"type":"object","name":"HelpTool","id":"p1249"}]}},"left":[{"type":"object","name":"LinearAxis","id":"p1236","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1238","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1237"},"major_label_policy":{"type":"object","name":"AllLabels","id":"p1239"}}}],"below":[{"type":"object","name":"LinearAxis","id":"p1229","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1231","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1230"},"major_label_policy":{"type":"object","name":"AllLabels","id":"p1232"}}}],"center":[{"type":"object","name":"Grid","id":"p1235","attributes":{"axis":{"id":"p1229"}}},{"type":"object","name":"Grid","id":"p1242","attributes":{"dimension":1,"axis":{"id":"p1236"}}}]}},{"type":"object","name":"Column","id":"p1272","attributes":{"children":[{"type":"object","name":"Slider","id":"p1267","attributes":{"js_property_callbacks":{"type":"map","entries":[["change:value",[{"type":"object","name":"CustomJS","id":"p1271","attributes":{"args":{"type":"map","entries":[["source",{"id":"p1209"}],["amp",{"id":"p1267"}],["freq",{"type":"object","name":"Slider","id":"p1268","attributes":{"js_property_callbacks":{"type":"map","entries":[["change:value",[{"id":"p1271"}]]]},"title":"Frequency","start":0.1,"end":10,"value":1,"step":0.1}}],["phase",{"type":"object","name":"Slider","id":"p1269","attributes":{"js_property_callbacks":{"type":"map","entries":[["change:value",[{"id":"p1271"}]]]},"title":"Phase","start":-6.4,"end":6.4,"value":0,"step":0.1}}],["offset",{"type":"object","name":"Slider","id":"p1270","attributes":{"js_property_callbacks":{"type":"map","entries":[["change:value",[{"id":"p1271"}]]]},"title":"Offset","start":-9,"end":9,"value":0,"step":0.1}}]]},"code":"\n    const A = amp.value\n    const k = freq.value\n    const phi = phase.value\n    const B = offset.value\n\n    const x = source.data.x\n    const y = Array.from(x, (x) =&gt; B + A*Math.exp(-x) * Math.sin(k*x+phi))\n    source.data = { x, y }\n"}}]]]},"title":"Amplitude","start":0.1,"end":10,"value":1,"step":0.1}},{"id":"p1268"},{"id":"p1269"},{"id":"p1270"}]}}]}}],"callbacks":{"type":"map"}}}'
                                }]
                            }
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-4",
                        index: 3,
                        textResponse: "Here is an Google Chart plot:\n\n[json-tag: code_execution_json_file.json]\n\nHope you find it useful.",
                        Vb: [],
                        Kb: {
                            ad: !1,
                            hc: [],
                            Zf: {
                                outcome: 3,
                                rK: 0,
                                cA: !0,
                                Ls: "python",
                                Rn: '\nfrom bokeh.io import output_file\nfrom bokeh.plotting import figure, show\n\n# prepare some data for an interactive line plot\nx = [1, 2, 3, 4]\ny = [1, 2, 4, 2]\n# create a new plot with a title and axis labels\np = figure(title="Simple line example", x_axis_label="x", y_axis_label="y")\n# add a line renderer with legend and line thickness to the plot\np.line(x, y, legend_label="Temp", line_width=2)\nshow(p)\n',
                                z6: [{
                                    hb: "[json-tag: code_execution_json_file.json]",
                                    mb: 0,
                                    vA: '{"title": "scatterplots_1_0_1695402218.4293082", "plot_type": "ScatterChart", "options": {"title": "Sleep duration per age by occupation", "hAxis": {"title": "Sleep duration", "minValue": "6.0", "maxValue": "8.5"}, "vAxis": {"title": "Age", "minValue": "30", "maxValue": "60"}}, "data": [["Sleep duration", "Software Engineer", "Doctor", "Sales Representative", "Teacher", "Nurse", "Engineer", "Accountant", "Scientist", "Lawyer", "Salesperson", "Manager"], [6.1, 27.0, null, null, null, null, null, null, null, null, null, null], [5.9, 28.0, null, null, null, null, null, null, null, null, null, null], [7.5, 35.0, null, null, null, null, null, null, null, null, null, null], [7.5, 35.0, null, null, null, null, null, null, null, null, null, null], [6.2, null, 28.0, null, null, null, null, null, null, null, null, null], [6.2, null, 28.0, null, null, null, null, null, null, null, null, null], [7.8, null, 29.0, null, null, null, null, null, null, null, null, null], [7.8, null, 29.0, null, null, null, null, null, null, null, null, null], [7.8, null, 29.0, null, null, null, null, null, null, null, null, null], [6.1, null, 29.0, null, null, null, null, null, null, null, null, null], [7.8, null, 29.0, null, null, null, null, null, null, null, null, null], [6.1, null, 29.0, null, null, null, null, null, null, null, null, null], [6.0, null, 29.0, null, null, null, null, null, null, null, null, null], [6.0, null, 29.0, null, null, null, null, null, null, null, null, null], [6.0, null, 29.0, null, null, null, null, null, null, null, null, null], [6.0, null, 29.0, null, null, null, null, null, null, null, null, null], [7.6, null, 30.0, null, null, null, null, null, null, null, null, null], [7.7, null, 30.0, null, null, null, null, null, null, null, null, null], [7.7, null, 30.0, null, null, null, null, null, null, null, null, null], [7.7, null, 30.0, null, null, null, null, null, null, null, null, null], [7.7, null, 30.0, null, null, null, null, null, null, null, null, null], [7.8, null, 30.0, null, null, null, null, null, null, null, null, null], [7.9, null, 30.0, null, null, null, null, null, null, null, null, null], [7.8, null, 30.0, null, null, null, null, null, null, null, null, null], [7.9, null, 30.0, null, null, null, null, null, null, null, null, null], [7.9, null, 30.0, null, null, null, null, null, null, null, null, null], [7.9, null, 30.0, null, null, null, null, null, null, null, null, null], [6.1, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [6.1, null, 31.0, null, null, null, null, null, null, null, null, null], [6.1, null, 31.0, null, null, null, null, null, null, null, null, null], [7.6, null, 31.0, null, null, null, null, null, null, null, null, null], [7.6, null, 31.0, null, null, null, null, null, null, null, null, null], [7.6, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.8, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.8, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.8, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [7.7, null, 31.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [7.6, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [7.7, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [7.7, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 32.0, null, null, null, null, null, null, null, null, null], [6.2, null, 32.0, null, null, null, null, null, null, null, null, null], [6.2, null, 32.0, null, null, null, null, null, null, null, null, null], [6.2, null, 32.0, null, null, null, null, null, null, null, null, null], [6.2, null, 32.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.1, null, 33.0, null, null, null, null, null, null, null, null, null], [6.1, null, 33.0, null, null, null, null, null, null, null, null, null], [6.1, null, 33.0, null, null, null, null, null, null, null, null, null], [6.1, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [6.0, null, 33.0, null, null, null, null, null, null, null, null, null], [7.3, null, 48.0, null, null, null, null, null, null, null, null, null], [7.3, null, 48.0, null, null, null, null, null, null, null, null, null], [8.1, null, 49.0, null, null, null, null, null, null, null, null, null], [8.1, null, 49.0, null, null, null, null, null, null, null, null, null], [8.2, null, 56.0, null, null, null, null, null, null, null, null, null], [8.2, null, 56.0, null, null, null, null, null, null, null, null, null], [5.9, null, null, 28.0, null, null, null, null, null, null, null, null], [5.9, null, null, 28.0, null, null, null, null, null, null, null, null], [6.3, null, null, null, 29.0, null, null, null, null, null, null, null], [6.7, null, null, null, 35.0, null, null, null, null, null, null, null], [6.7, null, null, null, 35.0, null, null, null, null, null, null, null], [7.1, null, null, null, 36.0, null, null, null, null, null, null, null], [7.1, null, null, null, 36.0, null, null, null, null, null, null, null], [7.2, null, null, null, 36.0, null, null, null, null, null, null, null], [7.2, null, null, null, 36.0, null, null, null, null, null, null, null], [7.2, null, null, null, 36.0, null, null, null, null, null, null, null], [6.6, null, null, null, 36.0, null, null, null, null, null, null, null], [7.2, null, null, null, 36.0, null, null, null, null, null, null, null], [6.6, null, null, null, 36.0, null, null, null, null, null, null, null], [6.8, null, null, null, 42.0, null, null, null, null, null, null, null], [6.8, null, null, null, 42.0, null, null, null, null, null, null, null], [6.7, null, null, null, 43.0, null, null, null, null, null, null, null], [6.7, null, null, null, 43.0, null, null, null, null, null, null, null], [6.7, null, null, null, 43.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.6, null, null, null, 44.0, null, null, null, null, null, null, null], [6.5, null, null, null, 44.0, null, null, null, null, null, null, null], [6.5, null, null, null, 44.0, null, null, null, null, null, null, null], [6.5, null, null, null, 44.0, null, null, null, null, null, null, null], [6.5, null, null, null, 44.0, null, null, null, null, null, null, null], [6.8, null, null, null, 45.0, null, null, null, null, null, null, null], [6.8, null, null, null, 45.0, null, null, null, null, null, null, null], [6.5, null, null, null, 45.0, null, null, null, null, null, null, null], [6.5, null, null, null, 45.0, null, null, null, null, null, null, null], [6.5, null, null, null, 45.0, null, null, null, null, null, null, null], [6.5, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.6, null, null, null, 45.0, null, null, null, null, null, null, null], [6.5, null, null, null, null, 29.0, null, null, null, null, null, null], [6.5, null, null, null, null, 29.0, null, null, null, null, null, null], [6.4, null, null, null, null, 30.0, null, null, null, null, null, null], [6.4, null, null, null, null, 30.0, null, null, null, null, null, null], [7.9, null, null, null, null, 31.0, null, null, null, null, null, null], [6.1, null, null, null, null, 37.0, null, null, null, null, null, null], [7.5, null, null, null, null, 37.0, null, null, null, null, null, null], [5.9, null, null, null, null, 48.0, null, null, null, null, null, null], [6.2, null, null, null, null, 49.0, null, null, null, null, null, null], [6.0, null, null, null, null, 49.0, null, null, null, null, null, null], [6.1, null, null, null, null, 49.0, null, null, null, null, null, null], [6.1, null, null, null, null, 49.0, null, null, null, null, null, null], [6.1, null, null, null, null, 49.0, null, null, null, null, null, null], [6.1, null, null, null, null, 49.0, null, null, null, null, null, null], [6.2, null, null, null, null, 49.0, null, null, null, null, null, null], [6.2, null, null, null, null, 49.0, null, null, null, null, null, null], [6.2, null, null, null, null, 49.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.0, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [6.1, null, null, null, null, 50.0, null, null, null, null, null, null], [7.1, null, null, null, null, 51.0, null, null, null, null, null, null], [6.0, null, null, null, null, 51.0, null, null, null, null, null, null], [6.1, null, null, null, null, 51.0, null, null, null, null, null, null], [6.1, null, null, null, null, 51.0, null, null, null, null, null, null], [8.1, null, null, null, null, 55.0, null, null, null, null, null, null], [8.1, null, null, null, null, 55.0, null, null, null, null, null, null], [8.1, null, null, null, null, 57.0, null, null, null, null, null, null], [8.2, null, null, null, null, 57.0, null, null, null, null, null, null], [8.2, null, null, null, null, 57.0, null, null, null, null, null, null], [8.2, null, null, null, null, 57.0, null, null, null, null, null, null], [8.2, null, null, null, null, 57.0, null, null, null, null, null, null], [8.2, null, null, null, null, 57.0, null, null, null, null, null, null], [8.1, null, null, null, null, 57.0, null, null, null, null, null, null], [8.1, null, null, null, null, 57.0, null, null, null, null, null, null], [8.1, null, null, null, null, 57.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 58.0, null, null, null, null, null, null], [8.0, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.2, null, null, null, null, 59.0, null, null, null, null, null, null], [8.2, null, null, null, null, 59.0, null, null, null, null, null, null], [8.2, null, null, null, null, 59.0, null, null, null, null, null, null], [8.2, null, null, null, null, 59.0, null, null, null, null, null, null], [8.0, null, null, null, null, 59.0, null, null, null, null, null, null], [8.0, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.0, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.0, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [8.1, null, null, null, null, 59.0, null, null, null, null, null, null], [7.5, null, null, null, null, null, 32.0, null, null, null, null, null], [7.5, null, null, null, null, null, 32.0, null, null, null, null, null], [7.2, null, null, null, null, null, 35.0, null, null, null, null, null], [7.2, null, null, null, null, null, 35.0, null, null, null, null, null], [7.3, null, null, null, null, null, 35.0, null, null, null, null, null], [7.3, null, null, null, null, null, 35.0, null, null, null, null, null], [7.3, null, null, null, null, null, 35.0, null, null, null, null, null], [7.3, null, null, null, null, null, 35.0, null, null, null, null, null], [7.8, null, null, null, null, null, 37.0, null, null, null, null, null], [7.8, null, null, null, null, null, 37.0, null, null, null, null, null], [6.5, null, null, null, null, null, 39.0, null, null, null, null, null], [7.3, null, null, null, null, null, 41.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [6.9, null, null, null, null, null, 43.0, null, null, null, null, null], [7.6, null, null, null, null, null, 43.0, null, null, null, null, null], [7.7, null, null, null, null, null, 43.0, null, null, null, null, null], [7.7, null, null, null, null, null, 43.0, null, null, null, null, null], [7.7, null, null, null, null, null, 43.0, null, null, null, null, null], [7.7, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.7, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [7.8, null, null, null, null, null, 43.0, null, null, null, null, null], [6.8, null, null, null, null, null, 44.0, null, null, null, null, null], [8.3, null, null, null, null, null, 50.0, null, null, null, null, null], [8.5, null, null, null, null, null, 51.0, null, null, null, null, null], [8.5, null, null, null, null, null, 51.0, null, null, null, null, null], [8.5, null, null, null, null, null, 51.0, null, null, null, null, null], [8.5, null, null, null, null, null, 51.0, null, null, null, null, null], [8.4, null, null, null, null, null, 52.0, null, null, null, null, null], [8.4, null, null, null, null, null, 52.0, null, null, null, null, null], [8.4, null, null, null, null, null, 52.0, null, null, null, null, null], [8.3, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.3, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.3, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.3, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.5, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 53.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.4, null, null, null, null, null, 54.0, null, null, null, null, null], [8.5, null, null, null, null, null, 54.0, null, null, null, null, null], [7.2, null, null, null, null, null, null, 32.0, null, null, null, null], [7.2, null, null, null, null, null, null, 35.0, null, null, null, null], [7.2, null, null, null, null, null, null, 36.0, null, null, null, null], [7.1, null, null, null, null, null, null, 36.0, null, null, null, null], [7.2, null, null, null, null, null, null, 36.0, null, null, null, null], [7.1, null, null, null, null, null, null, 36.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.2, null, null, null, null, null, null, 37.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [7.1, null, null, null, null, null, null, 38.0, null, null, null, null], [8.0, null, null, null, null, null, null, 39.0, null, null, null, null], [8.0, null, null, null, null, null, null, 39.0, null, null, null, null], [7.2, null, null, null, null, null, null, 40.0, null, null, null, null], [7.2, null, null, null, null, null, null, 40.0, null, null, null, null], [6.5, null, null, null, null, null, null, 52.0, null, null, null, null], [6.5, null, null, null, null, null, null, 52.0, null, null, null, null], [6.6, null, null, null, null, null, null, 52.0, null, null, null, null], [6.6, null, null, null, null, null, null, 52.0, null, null, null, null], [6.6, null, null, null, null, null, null, 52.0, null, null, null, null], [6.6, null, null, null, null, null, null, 52.0, null, null, null, null], [6.2, null, null, null, null, null, null, null, 33.0, null, null, null], [6.2, null, null, null, null, null, null, null, 33.0, null, null, null], [5.8, null, null, null, null, null, null, null, 34.0, null, null, null], [5.8, null, null, null, null, null, null, null, 34.0, null, null, null], [7.4, null, null, null, null, null, null, null, null, 35.0, null, null], [7.4, null, null, null, null, null, null, null, null, 37.0, null, null], [7.4, null, null, null, null, null, null, null, null, 37.0, null, null], [7.4, null, null, null, null, null, null, null, null, 37.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.3, null, null, null, null, null, null, null, null, 38.0, null, null], [7.1, null, null, null, null, null, null, null, null, 38.0, null, null], [7.1, null, null, null, null, null, null, null, null, 38.0, null, null], [7.1, null, null, null, null, null, null, null, null, 38.0, null, null], [7.1, null, null, null, null, null, null, null, null, 38.0, null, null], [7.4, null, null, null, null, null, null, null, null, 38.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [6.9, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.2, null, null, null, null, null, null, null, null, 39.0, null, null], [7.9, null, null, null, null, null, null, null, null, 40.0, null, null], [7.9, null, null, null, null, null, null, null, null, 40.0, null, null], [7.6, null, null, null, null, null, null, null, null, 41.0, null, null], [7.1, null, null, null, null, null, null, null, null, 41.0, null, null], [7.1, null, null, null, null, null, null, null, null, 41.0, null, null], [7.7, null, null, null, null, null, null, null, null, 41.0, null, null], [7.7, null, null, null, null, null, null, null, null, 41.0, null, null], [7.7, null, null, null, null, null, null, null, null, 41.0, null, null], [7.7, null, null, null, null, null, null, null, null, 41.0, null, null], [7.7, null, null, null, null, null, null, null, null, 41.0, null, null], [7.6, null, null, null, null, null, null, null, null, 41.0, null, null], [7.6, null, null, null, null, null, null, null, null, 41.0, null, null], [7.6, null, null, null, null, null, null, null, null, 41.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [7.8, null, null, null, null, null, null, null, null, 42.0, null, null], [6.5, null, null, null, null, null, null, null, null, null, 42.0, null], [6.3, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.4, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.5, null, null, null, null, null, null, null, null, null, 43.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.3, null, null, null, null, null, null, null, null, null, 44.0, null], [6.4, null, null, null, null, null, null, null, null, null, 44.0, null], [6.5, null, null, null, null, null, null, null, null, null, 44.0, null], [6.9, null, null, null, null, null, null, null, null, null, null, 45.0]]}'
                                }]
                            }
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_YOUR_DEFAULT_LOCATION",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "youtube_channel":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some channels about cute cats from Youtube:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "Kittisaurus",
                                    ei: "@Kittisaurus",
                                    url: "https://www.youtube.com/@Kittisaurus",
                                    Wy: "//yt3.googleusercontent.com/ytc/AOPolaQANjJvKWpYDUfSTwy4w5rofqy2GrZ0ZcEKBv684Q=s176-c-k-c0x00ffffff-no-rj",
                                    yi: ["Welcome to Pets Hub funny animals channel \u2665  You can enjoy best funny cats and dogs videos ever!Thanks for watching my videos \ud83d\ude0d\ud83d\ude0d\ud83d\ude0d"],
                                    resultType: 1
                                }],
                                Wl: "https://www.youtube.com/results?search_query=cute%20cats&sp=EgIQAg%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Here are some channels about cute cats from Youtube:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "Kittisaurus",
                                    ei: "@Kittisaurus",
                                    url: "https://www.youtube.com/@Kittisaurus",
                                    Wy: "//yt3.googleusercontent.com/ytc/AOPolaQANjJvKWpYDUfSTwy4w5rofqy2GrZ0ZcEKBv684Q=s176-c-k-c0x00ffffff-no-rj",
                                    yi: ["Welcome to Pets Hub funny animals channel \u2665  You can enjoy best funny cats and dogs videos ever!Thanks for watching my videos \ud83d\ude0d\ud83d\ude0d\ud83d\ude0d"],
                                    resultType: 1
                                }, {
                                    title: "Cats Only Channel",
                                    ei: "@CatsOnlyChannel",
                                    url: "https://www.youtube.com/@CatsOnlyChannel",
                                    Wy: "//yt3.googleusercontent.com/bXiCww5Bjl9Mm72YJyDjVr0xHZdGLRP6u6gpuIFzz2A-Izwdeh0mJf5C_Q5h75Da7RjRpYxWqg=s176-c-k-c0x00ffffff-no-rj",
                                    yi: [""],
                                    resultType: 1
                                }, {
                                    title: "The Animals",
                                    ei: "@TheAnimalsUSA",
                                    url: "https://www.youtube.com/@TheAnimalsUSA",
                                    Wy: "//yt3.googleusercontent.com/jU2btx-46Aj3KVku8aeYIfGcAWeKy0Q7nupIJX1EPFY30EsLGuwAtQzzJzuWb5X73539ej3UgxI=s176-c-k-c0x00ffffff-no-rj",
                                    yi: ["\ud83d\ude3bThe channel is intended for cheerful and positive people like YOU!!! \ud83d\ude3b \ud83d\udca5On this channel you can see jokes with cats, dogs, as well as with other animals. \ud83d\ude3dThe newest and top videos on YouTube!!!\ud83d\ude07If you subscribe, we will be very happy.\ud83d\ude07 500 SUBSCRIBERS \ud83d\ude3b 1000 SUBSCRIBERS \ud83d\ude3b 5000 SUBSCRIBERS  \ud83d\ude3b 10000 SUBSCRIBERS \ud83d\ude3b 20000 SUBSCRIBERS \ud83d\ude3b 50000 SUBSCRIBERS \ud83d\ude3b 100000 SUBSCRIBERS ? 200000 SUBSCRIBERS ? 500000 SUBSCRIBERS ? We make your day! We host the funniest and most interesting videos!"],
                                    resultType: 1
                                }],
                                Wl: "https://www.youtube.com/results?search_query=cute%20cats&sp=EgIQAg%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "youtube_playlist":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some cute cat playlists from Youtube:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "Cute kittens playlist",
                                    ei: "PLu8EB-prPnmKmdpnI5O9SZoPjh4FNzquX",
                                    url: "https://www.youtube.com/playlist?list=PLu8EB-prPnmKmdpnI5O9SZoPjh4FNzquX",
                                    jj: "Cute kittens",
                                    Fn: "CuteKittens",
                                    yi: ["Synthetic cute kittens This playlist is cutest kittens Aggregated playlist cute kittens Incorporate video cute kittens Playlist includes cute kittens Cutest kittens playlist"],
                                    resultType: 2
                                }],
                                Wl: "https://www.youtube.com/results?search_query=cute%20cats&sp=EgIQAw%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Here are some cute cat playlists from Youtube:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "Cute kittens playlist",
                                    ei: "PLu8EB-prPnmKmdpnI5O9SZoPjh4FNzquX",
                                    url: "https://www.youtube.com/playlist?list=PLu8EB-prPnmKmdpnI5O9SZoPjh4FNzquX",
                                    jj: "Cute kittens",
                                    Fn: "CuteKittens",
                                    yi: ["Synthetic cute kittens This playlist is cutest kittens Aggregated playlist cute kittens Incorporate video cute kittens Playlist includes cute kittens Cutest kittens playlist"],
                                    resultType: 2
                                }, {
                                    title: "Cat Videos of Cats Being Cats | The Dodo",
                                    ei: "PLLoPYaJqlcK5SzvX5rykYnsfLTxtXqLdf",
                                    url: "https://www.youtube.com/playlist?list=PLLoPYaJqlcK5SzvX5rykYnsfLTxtXqLdf",
                                    jj: "The Dodo",
                                    Fn: "TheDodo",
                                    yi: ["The most purrfect cat videos on YouTube. This playlist is full of songs that will make you smile and go \"aww!\". It's perfect for listening to while you're petting your cat, watching cat videos, or just feeling cute. The songs on this playlist range from upbeat and catchy to chill and relaxing. There's something for everyone, so whether you're a cat lover or just someone who appreciates cute things, you're sure to find something you'll enjoy."],
                                    resultType: 2
                                }],
                                Wl: "https://www.youtube.com/results?search_query=cute%20cats&sp=EgIQAw%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            case "youtube_single_video":
                return oS(this, pS(a, {
                    ub: "request-" + b,
                    Gb: [{
                        id: "response-" + b + "-1",
                        index: 0,
                        textResponse: "Here are some results for funny cat videos:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "20 Minutes of Adorable Kittens \ud83d\ude0d | BEST Compilation",
                                    ei: "y0sF5xhGreA",
                                    url: "http://www.youtube.com/watch?v=y0sF5xhGreA",
                                    jj: "The Pet Collective",
                                    Fn: "ThePetCollective",
                                    yi: ["Cute, cuddly, and utterly chaotic! These adorable kittens are jumping in the dog-pile in this collection of cute and hilarious kitty ..."],
                                    resultType: 0
                                }],
                                Wl: "https://www.youtube.com/results?search_query=funny%20cat%20videos&sp=EgIQAQ%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }, {
                        id: "response-" + b + "-2",
                        index: 1,
                        textResponse: "Here are some results for funny cat videos:\n\nhttp://googleusercontent.com/youtube_content/1\n\n",
                        Vb: [],
                        Kb: {
                            ad: !0,
                            hc: [],
                            fk: [],
                            an: [{
                                hb: "http://googleusercontent.com/youtube_content/1",
                                mb: 0,
                                title: "YT label for XXX",
                                Zl: {
                                    displayName: "YouTube",
                                    Oh: "https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg"
                                },
                                result: [{
                                    title: "20 Minutes of Adorable Kittens \ud83d\ude0d | BEST Compilation",
                                    ei: "y0sF5xhGreA",
                                    url: "http://www.youtube.com/watch?v=y0sF5xhGreA",
                                    jj: "The Pet Collective",
                                    Fn: "ThePetCollective",
                                    yi: ["Cute, cuddly, and utterly chaotic! These adorable kittens are jumping in the dog-pile in this collection of cute and hilarious kitty ..."],
                                    resultType: 0
                                }, {
                                    title: "Little Kitten Preschool Adventure Educational Games -Play Fun Cute Kitten Pet Care Learning #435",
                                    ei: "cWDKa8E6yOA",
                                    url: "http://www.youtube.com/watch?v=cWDKa8E6yOA",
                                    jj: "Mashiny Mashinki",
                                    Fn: "MashinyMashinki",
                                    yi: ['A primary school teacher that uses the app with her class said "The animation and gameplay are wonderful and our users fell in love with Little Kitten!" "Little Kitten & Friends is a great way for children to interact with a series of fun and educational games. Once the application has been used regularly parents can leave their children unsupported." "This certainly could be used in schools" Yay, Little Kitten is back and so excited about going to primary school! Our app \u201eLittle Kitten Preschool\u201c helps preparing children aged between 4 and 7 for their school start. Training perception, coordination and cognitive abilities - with Little Kitten this is a lot of fun!'],
                                    resultType: 0
                                }],
                                Wl: "https://www.youtube.com/results?search_query=funny%20cat%20videos&sp=EgIQAQ%253D%253D"
                            }]
                        },
                        oc: 0,
                        Cc: !1,
                        Gc: !1
                    }],
                    factualityQueries: [{
                        text: "Query 1 this is a really long factuality query and it should be cut off by ellipses.",
                        source: "source_1"
                    }, {
                        text: "Query 2",
                        source: "source_2"
                    }],
                    Vc: [],
                    Ug: {
                        Tf: "Mountain View, CA, USA",
                        Rf: "SWML_DESCRIPTION_FROM_YOUR_INTERNET_ADDRESS",
                        og: !1
                    },
                    Ad: "response-" + b + "-1"
                }));
            default:
                return oS(this, pS(a, _.qr(b, c)))
            }
        }