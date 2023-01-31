function my_defaults(position)
    set(gca, 'FontSize', 13, 'LineWidth', 2);
    box off
    if nargin == 1
        set(gcf, 'Position', position)
    end
end