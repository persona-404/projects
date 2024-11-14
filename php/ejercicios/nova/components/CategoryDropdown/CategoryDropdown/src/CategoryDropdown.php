<?php

namespace Pch\CategoryDropdown;

use App\Category;
use Laravel\Nova\Fields\Field;

class CategoryDropdown extends Field
{
    /**
     * The field's component.
     *
     * @var string
     */
    public $component = 'category-dropdown';

    /**
     * Get all categories with as many subcategories as added
     * 
     * @return categories list
     */
    public function all()
    {
    	$data = Category::with('children')->orderBy('name', 'asc')->get();

        $categories = [];

        $level = 0;
        foreach ($data as $key => $category) {
            if (is_null($category->parent_id)) {
                $categories[] = ['id' => $category->id, 'name' => $category->name];

                if (!$category->children->isEmpty()) {
                    $categories = $this->findChildren($category->children, $level, $categories);
                }
            }
        }

    	return $this->withMeta([
    		'categories' => $categories
    	]);
    }

    /**
     * Find children of parent and return it's subcategories
     * 
     * @param  $children   - current children 
     * @param  $level      - count levels to add dashes to symbolize if it's subcategory
     * @param  $categories - current categories info
     * 
     * @return array $categories
     */
    private function findChildren($children, $level, $categories) 
    {
        $level++;

        foreach ($children as $child) {
            $category = str_repeat('-', $level);
            $category .= ' ' . $child->name;

            $categories[] = ['id' => $child->id, 'name' => $category];

            if (!$child->children->isEmpty()) {
                $categories = $this->findChildren($child->children, $level, $categories);
            } 
        }

        return $categories;
    }
}
