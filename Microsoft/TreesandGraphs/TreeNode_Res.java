package Microsoft.TreesandGraphs;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/** Binary Tree Inorder Traversal, Morrise Traversal */
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

/* Use stacks instead, going to last most node and placing it on a stack, then popping. */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> li = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;


        return li;
    }
}