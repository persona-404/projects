<template>
    <default-field :field="field" :errors="errors">
        <template slot="field">
            <select
                :id="field.name"
                type="select"
                class="w-full form-control form-input form-input-bordered"
                v-model="value"
            >
                <option value="" disabled selected>Select Category</option>
                <option v-for="(category, key) in field.categories" :value="category.id"> {{ category.name }} </option>

            </select>

        </template>
    </default-field>
</template>

<script>
import { FormField, HandlesValidationErrors } from 'laravel-nova'

export default {
    mixins: [FormField, HandlesValidationErrors],

    props: ['resourceName', 'resourceId', 'field'],

    methods: {
        /*
         * Set the initial, internal value for the field.
         */
        setInitialValue() {
            this.value = this.field.value || ''
        },

        /**
         * Fill the given FormData object with the field's internal value.
         */
        fill(formData) {
            formData.append(this.field.attribute, this.value || '')
        },

        /**
         * Update the field's internal value.
         */
        handleChange(value) {
            this.value = value
        },

        /**
         * 
         */
        createChildren($value) {

        }
    },
}
</script>
