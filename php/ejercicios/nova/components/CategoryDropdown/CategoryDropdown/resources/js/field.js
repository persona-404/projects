Nova.booting((Vue, router, store) => {
    Vue.component('index-category-dropdown', require('./components/IndexField'))
    Vue.component('detail-category-dropdown', require('./components/DetailField'))
    Vue.component('form-category-dropdown', require('./components/FormField'))
})
