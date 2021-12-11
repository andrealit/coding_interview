package Microsoft.TreesandGraphs;
import java.util.ArrayList;
import java.util.List;

/** Binary Tree Inorder Traversal */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> li = new ArrayList<>();
        helper(root, li);
        return li;
    }
    public void helper(TreeNode root, List<Integer> li) {
        if (root != null) {
            helper(root.left, li);
            li.add(root.val);
            helper(root.right, li);
        }
    }
}