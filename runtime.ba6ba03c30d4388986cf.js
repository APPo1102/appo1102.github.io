( () => {
    "use strict";
    var e, r = {}, o = {};
    function n(e) {
        var t = o[e];
        if (void 0 !== t)
            return t.exports;
        var i = o[e] = {
            id: e,
            loaded: !1,
            exports: {}
        };
        return r[e].call(i.exports, i, i.exports, n),
        i.loaded = !0,
        i.exports
    }
    n.m = r,
    e = [],
    n.O = (r, o, t, i) => {
        if (!o) {
            var l = 1 / 0;
            for (u = 0; u < e.length; u++) {
                for (var [o,t,i] = e[u], a = !0, s = 0; s < o.length; s++)
                    (!1 & i || l >= i) && Object.keys(n.O).every((e => n.O[e](o[s]))) ? o.splice(s--, 1) : (a = !1,
                    i < l && (l = i));
                if (a) {
                    e.splice(u--, 1);
                    var f = t();
                    void 0 !== f && (r = f)
                }
            }
            return r
        }
        i = i || 0;
        for (var u = e.length; u > 0 && e[u - 1][2] > i; u--)
            e[u] = e[u - 1];
        e[u] = [o, t, i]
    }
    ,
    n.n = e => {
        var r = e && e.__esModule ? () => e.default : () => e;
        return n.d(r, {
            a: r
        }),
        r
    }
    ,
    n.d = (e, r) => {
        for (var o in r)
            n.o(r, o) && !n.o(e, o) && Object.defineProperty(e, o, {
                enumerable: !0,
                get: r[o]
            })
    }
    ,
    n.g = function() {
        if ("object" == typeof globalThis)
            return globalThis;
        try {
            return this || new Function("return this")()
        } catch (e) {
            if ("object" == typeof window)
                return window
        }
    }(),
    n.o = (e, r) => Object.prototype.hasOwnProperty.call(e, r),
    n.nmd = e => (e.paths = [],
    e.children || (e.children = []),
    e),
    ( () => {
        var e = {
            121: 0
        };
        n.O.j = r => 0 === e[r];
        var r = (r, o) => {
            var t, i, [l,a,s] = o, f = 0;
            if (l.some((r => 0 !== e[r]))) {
                for (t in a)
                    n.o(a, t) && (n.m[t] = a[t]);
                if (s)
                    var u = s(n)
            }
            for (r && r(o); f < l.length; f++)
                i = l[f],
                n.o(e, i) && e[i] && e[i][0](),
                e[i] = 0;
            return n.O(u)
        }
          , o = self.webpackChunklegion_solver = self.webpackChunklegion_solver || [];
        o.forEach(r.bind(null, 0)),
        o.push = r.bind(null, o.push.bind(o))
    }
    )(),
    n.nc = void 0
}
)();
